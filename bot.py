import logging
import config

from aiogram import Bot,Dispatcher,executor,types
import markups as nav

#bot init
bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot) 

#Комманда старт
@dp.message_handler(commands=["start"], commands_prefix="!/" )
async def start(message):
    await message.reply('Привет друг! Чтобы посмотреть доступные вакансии нажми <Найти>\nЧтобы добавить свою вакансию нажми <Добавить вакансию> ', reply_markup = nav.mainMenu) 
#Выводимая на экран кнопка- Найти
@dp.message_handler(commands=["Найти"], commands_prefix="!/" )
async def Найти(message):
    await message.reply ('Вот список профессий:', reply_markup = nav.Proffessions)
#Выводимая на экран кнопка- Главное_меню(возвращает к началу)
@dp.message_handler(commands=["Главное_меню"], commands_prefix="!/" )
async def Главное_меню(message):
    await message.reply ('Возвращаемся в Главное меню', reply_markup = nav.mainMenu)
#Выводимая на экран кнопка- Добавить вакансию
@dp.message_handler(commands=["Добавить_вакансию"], commands_prefix="!/" )
async def Добавить_вакансию(message):
    await message.reply ('Вот список профессий:', reply_markup = nav.Proffessions)






#long-poll
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)