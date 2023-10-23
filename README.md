## VRChat cache scanner (PYTHON3)

**Prerequisites:**

1. Ensure you have Python 3 installed on your system. If not, you can download and install it from the [Python official website](https://www.python.org/downloads/).

**Instructions:**

```python
# Use in CMD "Pip install requests" and "pip install time"

# Open the `scanner.py` script using a text editor of your choice.

# Locate the line that defines the `discord_webhook_url` variable. It will look like this:
   
discord_webhook_url = 'https://discord.com/api/webhooks/your_webhook_here'

# Replace `'https://discord.com/api/webhooks/your_webhook_here'` with your actual Discord webhook URL. Make sure you keep the single quotes around the URL.

# Save the changes to the `scanner.py` file.

# Open a terminal or command prompt on your system.

# Navigate to the directory where the `scanner.py` script is located using the `cd` command. For example, if `scanner.py` is in the `D:\Logger` directory, you can navigate to it with:
   
cd D:\Logger

# Once you are in the correct directory, execute the script using the following command:

python3 scanner.py

# The script will start running and will search for IDs in the specified folder. It will also send unique IDs to the specified Discord webhook URL in batches.

# The script will continue to run in the background. It will search for IDs at regular intervals and send them to Discord if new IDs are found.

**Note:**

- Make sure you have an active internet connection to send messages to the Discord webhook.

That's it! You've successfully set up and executed the `scanner.py` script with your Discord webhook. It will continuously search for IDs and send them to your Discord server as it finds them.

This will send the IDs to a Discord webhook every 50 IDs, so you should have a minimum of 50 avatars in the cache. The response will not be sent instantly but when it reaches 50, it will be sent. You can edit this yourself by editing line 23, where it says 'batch_size = 50'. The number '50' indicates how many IDs will be sent in each message (It is recommended to use a high number to avoid spam).
