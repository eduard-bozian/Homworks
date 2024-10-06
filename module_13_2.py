from aiogram import Bot, Dispatcher, executor, types
from aiogram.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storge= MemoryStorage())

@dp.message_hendler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')

@dp.message_hendler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_hendler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
