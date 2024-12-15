import asyncio
import logging
import sys
from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())