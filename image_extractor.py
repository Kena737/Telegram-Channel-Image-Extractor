from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
import os

# Replace with your Telegram API credentials
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
channel_username = 'channel_username_or_link'  # Example: 'https://t.me/example_channel' or 'example_channel'

# Create a folder to save images
download_folder = "downloaded_images"
os.makedirs(download_folder, exist_ok=True)

# Connect and download images
with TelegramClient('anon', api_id, api_hash) as client:
    for message in client.iter_messages(channel_username):
        if message.media and isinstance(message.media, MessageMediaPhoto):
            client.download_media(message, file=os.path.join(download_folder, f"{message.id}.jpg"))
            print(f"Downloaded image {message.id}")
