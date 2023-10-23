import os
import re
import requests
import time

#CHANGE THIS
target_folder = r'C:\Users\YOUR USERNAME\AppData\LocalLow\VRChat\VRChat\Cache-WindowsPlayer'


pattern = re.compile(r'avtr_[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')

#CHANGE THIS
output_file_path = 'D:\Logger\scan.txt'


unique_results = set()

# Webhook
discord_webhook_url = 'https://discord.com/api/webhooks/your_webhook_here'


def send_results_to_discord(webhook_url, results):
    batch_size = 50  

    results_list = list(results)
    while results_list:
        batch = results_list[:batch_size]
        results_list = results_list[batch_size:]
        message = "\n".join(batch)

        
        payload = {'content': message}

        
        response = requests.post(webhook_url, json=payload)

        if response.status_code != 204:
            print(f'Error al enviar el mensaje: {response.status_code}')
        else:
            print(f'Mensaje enviado a Discord: {message}')


if os.path.exists(output_file_path):
    with open(output_file_path, 'r', encoding='utf-8') as existing_output_file:
        for line in existing_output_file:
            unique_results.add(line.strip())


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
                                print(f'Log ready: {match}')

                                
                                print(f'ID Captured: {match}')

while True:
    print('Starting search...')
    search_and_save_results(target_folder)
    print('Search complete.')

    if unique_results:
        print('Uploading to Discord...')
        send_results_to_discord(discord_webhook_url, unique_results)
        print('Uploaded to Discord.')

    time.sleep(3600)
