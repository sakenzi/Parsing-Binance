import asyncio
import requests
from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import aiohttp


TOKEN = config('TOKEN')
DJANGO_API_URL_1 = config('DJANGO_API_URL_1')
DJANGO_API_URL_2 = config('DJANGO_API_URL_2')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот аналитики криптовалюты!")
    await message.answer("Напиши имя криптовалюты!")

@dp.message()
async def get_crypto_name(message:Message):
    try:
        crypto_name = message.text.strip()

        if crypto_name.isalpha():
            await message.answer(f"Ищем информацию о криптовалюте: {crypto_name} ... ")
            async with aiohttp.ClientSession() as session:
                async with session.get(DJANGO_API_URL_2, params={'short_name': crypto_name}) as response:
                    if response.status == 200:
                        data = await response.json()
                        if "data" in data:
                            result = data["data"]
                            response_text = "\n".join([f"{key}: {value}" for key, value in result.items()])
                            await message.answer(f"Информация о криптовалюте {crypto_name}:\n{response_text}")
                        else:
                            await message.answer(f"Информация о криптовалюте {crypto_name} не найдена.")
                    else:
                        await message.answer(f"Ошибка при получении данных о криптовалюте: {response.status}")
        else:
            await message.answer("Пожалуйста, введите корректное имя криптовалюты (только буквы).")
            
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")

    # button1 = InlineKeyboardButton(text="Выберите криптовалюту", callback_data="button")
    
    # keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1]])

    

# @dp.callback_query()
# async def handle_callback(callback_query: CallbackQuery):
#     if callback_query.data == "button":
#         await callback_query.message.answer("Напишите название криптовалюты!")
    
#     await callback_query.answer()

@dp.message(Command("set_interval"))
async def set_interval(message: Message):
    try:
        interval = int(message.text.split()[1])
        
        response = requests.post(DJANGO_API_URL_1, json={"interval_minutes": interval})
        
        if response.status_code == 200:
            await message.answer(f"Интервал парсинга успешно изменён на {interval} минут!")
        else:
            await message.answer(f"Ошибка при обновлении интервала: {response.text}")
    except IndexError:
        await message.answer("Укажите интервал в минутах. Например: /set_interval 10")
    except ValueError:
        await message.answer("Неверный формат. Укажите целое число.")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
