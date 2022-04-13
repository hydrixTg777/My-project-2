from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Callback

@Client.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text =f" Hello {msg.from_user.mention} 😁",
        )

    elif msg.data == "start1":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text=f"**Hello** ||{msg.from_user.mention}||Welcome to my world🌍\n\n**My name is** [My Craft](t.me/mycraftprojectbot)\n__This is my first pyrogram project__ 😜\n~~Click help for find my tools~~ ⛏️\nJoin my Channel: [TG](t.me/tg_galaxy)",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton ("➕Add me to group➕", url="http://t.me/Mycraftprojectbot?startgroup=botstart")
               ],[
               InlineKeyboardButton("👥 Group", url="https://t.me/songdownload_group"),
               InlineKeyboardButton("📚 Help", callback_data="help")
               ],[
               InlineKeyboardButton("🧑‍💻 My Dev", url="https://t.me/Hydrix777"),
               InlineKeyboardButton("🔰 About", callback_data="about")
               ],[
               InlineKeyboardButton("🏃 Close", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "help":

        await msg.message.reply_chat_action("Typing")
        await asyncio.sleep(1)

        reply1 = await msg.message.reply_text("▪️▫️▫️")
        await asyncio.sleep(0.5)
        reply2 = await reply1.edit("▪️▪️▫️")
        await asyncio.sleep(0.5)
        reply3 = await reply2.edit("▪️▪️▪️")
        await asyncio.sleep(0.5)
        await reply3.delete()



        await msg.message.edit(
            text="**My Tools**",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("Info", callback_data="ids"),
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start")
               ],[
               InlineKeyboardButton("« Back", callback_data="start1"),
               InlineKeyboardButton("✗ Close ✗", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "ids":
        await msg.message.edit(
            text="/id : to get your ID\n/info : to get your information ℹ️\n/ginfo - To get group information 👥\n/dc : to get your datacenter 🗄️",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« Back", callback_data="start1")
               ]]
            )
        )

    elif msg.data == "about":

        reply1 = await msg.message.reply_text("▪️▫️▫️")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("▪️▪️▫️")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("▪️▪️▪️")
        await asyncio.sleep(0.5)

        await reply3.delete()

        await msg.message.edit(
            text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖 **Bot Nᴀᴍᴇ**: [Mʏ Craft](https://t.me/Mycraftprojectbot)\n├🧑‍💻 **Mʏ Dᴇᴠ**: [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📡 **Sᴇʀᴠᴇʀ**: [Heroku](https://heroku.app)\n├🔣 **Language**: [Python-3](https://python.org/)\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« Back", callback_data="start1")
              ]]
            )
        )

    elif msg.data == "delete":
        await msg.message.delete()
