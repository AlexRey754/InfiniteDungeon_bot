from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio

import time

from config import TOKEN

bot = Bot(token=TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer('Приветик Друг!')

if __name__ == '__main__':
    executor.start_polling(dp)
