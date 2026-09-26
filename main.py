from pyrogram import Client, filters
import os
import threading
from flask import Flask

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("abhi_tech_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Render ke liye Web Server taaki OFF na ho
web_app = Flask(__name__)
@web_app.route('/')
def home():
    return "Bot Live Ho Gaya! Made By Tech Abhi"

def run_web():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot Live Ho Gaya! 🚀 Made by Tech Abhi")

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    app.run()
