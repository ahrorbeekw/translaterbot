import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import time
from googletrans import Translator
translator = Translator()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = 'Bot tokeni'

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/800px-Google_Translate_logo.svg.png',
                                    caption="🌐Google transga hush kelibsiz!‼️‼️ \n \n⚜️<b>Ingilizcha so'z kiriting⚜️ </b>\n<b>⚜️Uzbekcha tarjima qilaman⚜️ </b>\n\nADMIN: <B>@ahrorbeek007</b>🌐")

@dp.message()
async def echo_handler(message: Message) -> None:
    
    try:
        translate_channel = translator.translate(f"{message.text}", src='en', dest='uz')
        await message.answer(f'<b>⚜️Tarjima</b>: <i>{translate_channel.text}</i>')
    except:
        await message.answer("Soz topilmadi!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


#pip install googletrans==3.1.0a0
