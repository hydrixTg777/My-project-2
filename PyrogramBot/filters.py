from pyrogram import Client, filters


@Client.on_message(filters.regex("hello"))
async def regex(bot, hydrix):
    await hydrix.reply_text("hello")
