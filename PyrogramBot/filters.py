from pyrogram import Client, filters


@Client.on_message(filters.regex("hello"))
async def regex(bot, msg):
    await msg.reply_text("hello")
