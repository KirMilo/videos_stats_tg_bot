import asyncio

from core.config import settings
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

from llm.service import get_answer

bot = Bot(token=settings.tg.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот-аналитик видео. Чем могу помочь?")


@dp.message()
async def chat_handler(message: Message):
    answer = await get_answer(message.text)
    await message.answer(answer)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot is running...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is stopped.")
