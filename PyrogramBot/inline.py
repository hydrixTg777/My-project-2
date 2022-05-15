from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton  



@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[

            InlineQueryResultArticle(
                title="HyDrix",
                description="Click Here",
                thumb_url="https://telegra.ph/file/27b70110ca3c941f61252.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""okk daaa"""
                ),
                reply_markup=InlineKeyboardMarkup(
                    InlineKeyboardButton("Hydrix", url="t.me/tg_galaxy")
                    ]]
                )
            ),

            InlineQueryResultArticle(
                title="HyDrix",
                description="Click Here",
                thumb_url="https://telegra.ph/file/27b70110ca3c941f61252.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""okk daaa"""
                )
            )

        ],
        cache_time=0
    )
