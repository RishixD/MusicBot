from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEJar1gfUPxtIX1OutHd1sOi37QRKjBTQACPgADiHb1PyaUZ16x2sykHwQ")
    await message.reply_text(
        f"""**Hey, I'm β‘ ππππππ πππππ πππ β’ β‘

I can play music in your group's voice call. Developed by [ππππππβ‘](https://t.me/ItzMeDEXTER).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π€π» ππΎππ πΌπ°πΊπ΄π π€π»", url="https://t.me/ItzMeDEXTER")
                  ],[
                    InlineKeyboardButton(
                        "π° πΆππΎππΏ π°", url="https://t.me/About_ItsMeDEXTER"
                    ),
                    InlineKeyboardButton(
                        "ποΈ π²πΎπΌπΌπ°π½π³π ποΈ", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π π°π³π³ ππΎ ππΎππ πΆππΎππΏ π", url="https://t.me/DEXTER_MUSIC_WORLD_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**β‘ ππππππ πππ β’ β‘ is on fire π₯ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΏπ»π°ππΈπ½πΆ π±π ππΎππ DADπ€π»", url="https://t.me/ItzMeDEXTER")
                ]
            ]
        )
   )


