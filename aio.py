import asyncio
import time

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
import os
from aiogram.filters import Command

from main import buttons_category
from parser import tilvizr
from configs import get_value

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(
    TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)
dp = Dispatcher()


@dp.message(Command('start'))
async def commans_start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu Alaykum <b>{full_name}</b> "
                         f"Texnomart* do'koniga hush kelibsiz🚀")
    await show_category_menu(message)


async def show_category_menu(message : Message):
    await message.answer('Kategorya tanlang ', reply_markup=buttons_category())


async def get_product_by_open_shop(message : Message):
    category_text = message.text

    category_key = get_value(category_text)
    if category_key in None:
        return await message.answer("Kechirsiz bu kategorya mavjud emas !")

    get_product = tilvizr(get_value(category_text))
    if not get_product:
        return await message.answer("Kechirasiz kategorya mahsuloti topilmadi")

    for product in get_product:
        image = product.get('rasm')
        title = product.get('title')
        credit_price = product.get('credit_price')
        price = product.get('price')

        time.sleep(0.5)

        await message.answer_photo(
            photo=image,
            caption=f"{title}\n\n{credit_price}\n\n{price}",
        )
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())