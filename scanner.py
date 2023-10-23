import os
import re
import requests
import time

# CHANGE THIS TO YOUR VRCHAT CACHE FOLDER
target_folder = r'C:\Users\YOUR USER\AppData\LocalLow\VRChat\VRChat\Cache-WindowsPlayer'

# Regular expression to find the exact string "avtr_" followed by a UUID
pattern = re.compile(r'avtr_[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')

# CHANGE THIS TO SELECT WHERE THE FILE WILL GO
output_file_path = 'C:\Logger\scan.txt'

# Set to store unique strings
unique_results = set()

# Discord Webhook URL
discord_webhook_url = 'https://discord.com/api/webhooks/your_webhook_here'

# Function to send results to Discord in batches
def send_results_to_discord(webhook_url, results):
    batch_size = 50  # Number of IDs per batch

    results_list = list(results)
    while results_list:
        batch = results_list[:batch_size]
        results_list = results_list[batch_size:]
        message = "\n".join(batch)

        # Create the message payload
        payload = {'content': message}

        # Send the message to the webhook
        response = requests.post(webhook_url, json=payload)

        if response.status_code != 204:
            print(f'Error sending the message: {response.status_code}')
        else:
            print(f'Message sent to Discord: {message}')

# Check if the output file already exists
if os.path.exists(output_file_path):
    with open(output_file_path, 'r', encoding='utf-8') as existing_output_file:
        for line in existing_output_file:
            unique_results.add(line.strip())

# Function to search and save results in real-time to a file
def search_and_save_results(folder):
    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
                    for line in input_file:
                        matches = pattern.findall(line)
                        for match in matches:
                            if match not in unique_results:
                                unique_results.add(match)
                                output_file.write(match + '\n')
                                print(f'Record found and saved: {match}')

                                # Add this line to display each ID in the console
                                print(f'Captured ID: {match}')

# Continuous loop to search and send results in batches
while True:
    print('Starting search and logging...')
    search_and save_results(target_folder)
    print('Search and logging completed.')

    if unique_results:
        print('Sending results to Discord...')
        send_results_to_discord(discord_webhook_url, unique_results)
        print('Results sent to Discord.')

    time.sleep(3600)  # Wait for 1 hour before the next search
