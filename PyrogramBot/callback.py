from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio

# Callback

@Client.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text =f" Hello {msg.from_user.mention} π",
        )

    elif msg.data == "start1":

        await msg.message.reply_chat_action("Typing")
        await asyncio.sleep(1)

        reply1 = await msg.message.reply_text("ββββ")
        await asyncio.sleep(0.5)
        reply2 = await reply1.edit("ββββ")
        await asyncio.sleep(0.5)
        reply3 = await reply2.edit("ββββ")
        await asyncio.sleep(0.5)
        reply4 = await reply3.edit("ββββ")
        await asyncio.sleep(0.5)
        await reply4.delete()



        await msg.message.edit(
            text=f"**Hello** ||{msg.from_user.mention}||Welcome to my worldπ\n\n**My name is** [My Craft](t.me/mycraftprojectbot)\n__This is my first pyrogram project__ π\n~~Click help for find my tools~~ βοΈ\nJoin my Channel: [TG](t.me/tg_galaxy)",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton ("βAdd me to groupβ", url="http://t.me/Mycraftprojectbot?startgroup=botstart")
               ],[
               InlineKeyboardButton("π₯ Group", url="https://t.me/songdownload_group"),
               InlineKeyboardButton("π Help", callback_data="help")
               ],[
               InlineKeyboardButton("π§βπ» My Dev", url="https://t.me/Hydrix777"),
               InlineKeyboardButton("π° About", callback_data="about")
               ],[
               InlineKeyboardButton("π Close", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "help":

        await msg.message.reply_chat_action("Typing")
        await asyncio.sleep(1)

        reply1 = await msg.message.reply_text("ββββ")
        await asyncio.sleep(0.5)
        reply2 = await reply1.edit("ββββ")
        await asyncio.sleep(0.5)
        reply3 = await reply2.edit("ββββ")
        await asyncio.sleep(0.5)
        reply4 = await reply3.edit("ββββ")
        await asyncio.sleep(0.5)
        await reply4.delete()


        await msg.message.edit(
            text="**My Tools**",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("Info", callback_data="ids"),
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start")
               ],[
               InlineKeyboardButton("Β« Back", callback_data="start1"),
               InlineKeyboardButton("β Close β", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "ids":
        await msg.message.edit(
            text="/id : to get your ID\n/info : to get your information βΉοΈ\n/ginfo - To get group information π₯\n/dc : to get your datacenter ποΈ",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("Β« Back", callback_data="start1")
               ]]
            )
        )

    elif msg.data == "about":

        await msg.message.reply_chat_action("Typing")
        await asyncio.sleep(1)

        reply1 = await msg.message.reply_text("βͺοΈβ«οΈβ«οΈ")
        await asyncio.sleep(0.5)
        reply2 = await reply1.edit("βͺοΈβͺοΈβ«οΈ")
        await asyncio.sleep(0.5)
        reply3 = await reply2.edit("βͺοΈβͺοΈβͺοΈ")
        await asyncio.sleep(0.5)
        await reply3.delete()



        await msg.message.edit(
            text="β­ββββ[α΄Κα΄α΄α΄]βββββ\nβπ€ **Bot Nα΄α΄α΄**: [MΚ Craft](https://t.me/Mycraftprojectbot)\nβπ§βπ» **MΚ Dα΄α΄ **: [HΚα΄ΚΙͺx](https://t.me/Hydrix777)\nβπ‘ **Sα΄Κα΄ α΄Κ**: [Heroku](https://heroku.app)\nβπ£ **Language**: [Python-3](https://python.org/)\nβ°ββββββββββββ",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("Β« Back", callback_data="start1")
              ]]
            )
        )

    elif msg.data == "delete":
        await msg.message.delete()
