from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


bot = Bot(token='')
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton('Рассчитать'))
keyboard.add(types.KeyboardButton('Информация'))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, который поможет тебе рассчитать рост и вес твоего ребенка.', reply_markup=keyboard)

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer('Введите возраст ребенка в годах:')
    await message.answer('Введите рост ребенка в сантиметрах:')
    await message.answer('Введите вес ребенка в килограммах:')

@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer('Информация о боте')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

