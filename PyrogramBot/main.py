from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.types import CallbackQuery
import random
from pyrogram.errors import UserNotParticipant


force_subhydra = "Tg_Galaxy"




START_MESSAGE = """
**Hello** ||{}||Welcome to my world🌍

**My name is** <a href="t.me/Mycraftprojectbot">My Craft</a> 
__This is my first pyrogram project__ 😜
~~Click help for find my tools~~ ⛏️
`Join my Channel` : <a href="t.me/tg_galaxy">TG</a>
"""

 
START_PHOTO = [
 "https://telegra.ph/file/6b4b3936e2d964c16cd1b.jpg",
 "https://telegra.ph/file/3556fb3dab26579466ac5.jpg",
 "https://telegra.ph/file/c0b61b64e247438f1a30b.jpg",
 "https://telegra.ph/file/1541a2c2e76dd63eb1daa.jpg",
 "https://telegra.ph/file/115105893e168223e5bc0.jpg",
 "https://telegra.ph/file/9d3a5ec8aab272b1e61a2.jpg",
 "https://telegra.ph/file/aac42f0ff1895b881e9dd.jpg"
]





@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    if force_subhydra:
        try:
            user = await bot. get_chat_member(force_subhydra, message.from_user.id)
            if user.status == "kick out":
                await message.reply_text("you are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="you are not subscribed my channel",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Update Channel", url=f"t.me/{force_subhydra}")
                 ]]
                )
            )
            return
    await message.reply_photo(
        photo=random.choice(START_PHOTO),
        caption=START_MESSAGE.format(message.from_user.mention),
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


@Client.on_message(filters.private & filters.command("info"))
async def id(bot, hydrix):
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIT52ISTo1D3dUZ8KNG-hLN5hWid6lSAALqFAACXongS2tWgvz0KigPHgQ"             
    )
    text = f"""
First Name : {hydrix.from_user.first_name}
Last Name : {hydrix.from_user.last_name}
User Name : @{hydrix.from_user.username}
ID : `{hydrix.from_user.id}`
Mention : {hydrix.from_user.mention}"""

    await hydrix.reply_text(text=text)


@Client.on_message(filters.group & filters.command("ginfo"))
async def demo(bot, hydrix):
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIUDmISWCSOoFk5ctVJNSHw_CWBQ2RvAAJeFwAC0UfgSy6uWe6YGw9HHgQ"             
    )
    text = f"""
Group Name : {hydrix.chat.title}
UserName : @{hydrix.chat.username}
Group ID : `{hydrix.chat.id}`"""


    await hydrix.reply_text(text=text)

@Client.on_message(filters.command("id"))
async def id(bot, hydrix):
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIT6WISTsdtVuRUOBGx5ec2pNWkmjejAALWFAACNzTgS_dLIpoeFnBvHgQ"             
    )
    text = f"""
<b>{hydrix.from_user.first_name}</b>your ID is : `{hydrix.from_user.id}`
"""


    await hydrix.reply_text(text=text)

@Client.on_message(filters.private & filters.command("dc"))
async def dc(bot, hydrix):
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIUXGISsh-8Iv9fYnUG_XCF8Xdh-76EAALWEQAC1GDhS0Xcwj7uV5qSHgQ"             
    )
    text = f"""
<b>{hydrix.from_user.first_name}</b>your DC is : `{hydrix.from_user.dc_id}`
"""


    await hydrix.reply_text(text=text)
