from pyrogram import Client, filters


@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_text("hi")
