from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

btnMain = KeyboardButton ('!Главное_меню')

#
btn1 = KeyboardButton ("!Найти")
btn2 = KeyboardButton ("!Добавить_вакансию")
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn1,btn2)

#

btn3 = KeyboardButton ("!Строительство")
btn4 = KeyboardButton ("!Торговля")
btn5 = KeyboardButton ("!Транспорт")
btn6 = KeyboardButton ("!Юриспруденция")
btn7 = KeyboardButton ("!Военная_служба")
btn8 = KeyboardButton ("!Здравохранение")
btn9 = KeyboardButton ("!IT")
Proffessions = ReplyKeyboardMarkup(resize_keyboard = True).add(btn3,btn4,btn5,btn6,btn7,btn8,btn9,btnMain)