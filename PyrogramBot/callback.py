from pyrogram.types import CallbackQuery
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




# Callback

@Client.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text =f" Hello {msg.from_user.mention} 😁",
        )

    elif msg.data == "help":
        await msg.message.edit(
            text="**My Tools**",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("Info", callback_data="ids"),
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start")
               ],[
               InlineKeyboardButton("🧑‍🦯 Exit", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "ids":
        await msg.message.edit(
            text="/id : to get your ID\n/info : to get your information ℹ️\n/ginfo - To get group information 👥\n/dc : to get your datacenter 🗄️",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🧑‍🦯 Exit", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "about":
        await msg.message.edit(
            text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖 **Bot Nᴀᴍᴇ**: [Mʏ Craft](https://t.me/Mycraftprojectbot)\n├🧑‍💻 **Mʏ Dᴇᴠ**: [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📡 **Sᴇʀᴠᴇʀ**: [Railway](https://Railway.app)\n├🔣 **Language**: [Python-3](https://python.org/)\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🧑‍🦯 Exit", callback_data="delete")
              ]]
            )
        )
    elif msg.data == "delete":
        await msg.message.delete()
