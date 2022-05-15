from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle



@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery) 
    await query.answer(
        results=[
            InlineQueryResultArticle(
                title="HyDrix",
                description="Click Here",
                input_message_content
