import json
import os
import sqlite3
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import StatesGroup, State

memory = MemoryStorage()
bot = Bot(token='5396098820:AAGY_1ThI4cmrSB9wLMYsZhEUHIc01cWywU')
dp = Dispatcher(bot, storage=memory)


class Sell_SWC(StatesGroup):
    pair = State()


class Buy_SWC(StatesGroup):
    buy_count = State()
    username = State()


def main_buttons():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.resize_keyboard = True
    buttons = ['Продать SWC',
               'Почему вам стоит нам доверять']
    keyboard.add(*buttons)
    return keyboard


def sell_buttons():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.resize_keyboard = True
    buttons = ['Продать SWC в USDT', 'Продать SWC в UAH', 'Продать SWC в RUB', 'Назад']
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(Text(equals='/start'))
async def start(msg: types.Message):
    await msg.answer("Добро пожаловать!\n\nВы зашли на надежный обменник SWC-USDT!\n\nЗдесь вы сможете легко продать свои SWC коины "
                     "по выгодному курсу")
    await msg.answer("В случае ошибок напишите /start")
    await msg.answer("Выберите действие:", reply_markup=main_buttons())


@dp.message_handler(Text(equals='Продать SWC'))
async def sell_swc(msg: types.Message):
    await msg.answer('Выберите пару обмена: ', reply_markup=sell_buttons())
    await Sell_SWC.pair.set()


@dp.message_handler(state=Sell_SWC.pair)
async def set_pair(msg: types.Message, state: FSMContext):
    if msg.text in ['Продать SWC в USDT', 'Продать SWC в UAH', 'Продать SWC в RUB', 'Назад']:
        await state.finish()
        if msg.text == 'Назад':
            await msg.answer('Главное меню', reply_markup=main_buttons())
        if msg.text == 'Продать SWC в USDT':
            await msg.answer(f'Текущий курс в USDT: 1 SWC = 0.20 $')
            await msg.answer('Вы должны отправить любое колличество swc от 5 Токенов а также в описание написать вашу карту для оплаты обмена')
            await msg.answer('После обмена SWC оплата произойдет в течение ближайших 12 часов', reply_markup=main_buttons())
        if msg.text == 'Продать SWC в UAH':
            await msg.answer(f'Текущий курс в USDT: 1 SWC = 7.5 UAH')
            await msg.answer('Вы должны отправить любое колличество swc от 5 Токенов а также в описание написать вашу карту для оплаты обмена')
            await msg.answer('После обмена SWC оплата произойдет в течение ближайших 12 часов', reply_markup=main_buttons())
        if msg.text == 'Продать SWC в RUB':
            await msg.answer(f'Текущий курс в USDT: 1 SWC = 17 RUB')
            await msg.answer('Вы должны отправить любое колличество swc от 5 Токенов а также в описание написать вашу карту для оплаты обмена')
            await msg.answer('После обмена SWC оплата произойдет в течение ближайших 12 часов', reply_markup=main_buttons())

@dp.message_handler(Text(equals='Почему вам стоит нам доверять'))
async def why(msg: types.Message):
    await msg.answer('Мы являемся честным обменником монет на валюту.\nНам нету смысла обманивать продавцов так как это осквернит наш обменник')

async def channel(msg: types.Message):
    inline_btn_1 = types.InlineKeyboardButton('Канал', url="https://t.me/luter_news")
    inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)
    await msg.answer("Наш канал с новостями и конкурсами👇", reply_markup=inline_kb1)


if __name__ == '__main__':
    executor.start_polling(dp)
