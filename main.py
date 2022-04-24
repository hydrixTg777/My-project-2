from pyrogram import Client
import os
from config import API_HASH, API_ID, BOT_TOKEN

Client = Client(
    "PyrogramBot",
    api_hash=API_HASH, 
    api_id=API_ID, 
    bot_token=BOT_TOKEN, 
    plugins=dict(root="PyrogramBot")
) 

Client.run()
