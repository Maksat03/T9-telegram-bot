import logging
logging.basicConfig(level=logging.INFO)

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ContentType, Message

from t9 import T9

bot = Bot(token='5205366808:AAHhZd463QLDfnSfxi0P72XrfsF0y1Qgo70', parse_mode='HTML')
dp = Dispatcher(bot)
t9 = T9()

@dp.message_handler(commands=['start'])
async def welcome(msg: Message):
	me = await bot.get_me()
	await msg.answer(f"Здравствуйте <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>. Я <i>{me.first_name}</i> T9 telegram bot. Вы можете написать мне текст и я могу его исправить.")

@dp.message_handler(content_types=ContentType.TEXT)
async def get_message(msg: Message):
	result = t9.fix(msg.text)
	if (result[0] > 0):
		await msg.reply(f"Неправильные слова: {result[1]}.\n\nИсправленный полный текст:\n{result[2]}.")
	else:
		await msg.reply("В тексте нет ошибок")

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)