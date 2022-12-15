import os
import webbrowser
import sys
import subprocess
import voiceBot
import random
import datetime
from datetime import datetime
from datetime import date
import re
from phrases import *
import wikipedia
import time






try:
    import requests #Это простая в использовании библиотека с множеством функций, начиная от передачи параметров в URL и заканчивая отправкой пользовательских заголовков и SSL-проверкой.
except:
    pass

# ЮТУБ
def youtubeStart():#Открывает браузер заданнный по уполчанию в системе с url указанным здесь
    webbrowser.open('https://www.youtube.com', new=2)



# ГУГЛ
def googleStart():
    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")



# ФИЛЬМЫ
def zetflix():

    strDate = datetime.now()
    webbrowser.open(f'https://{strDate.day}dec.zetfix.online/', new=2)



# ДНЕВНИК
def eljur():
    webbrowser.open('https://kip.eljur.ru/authorize', new=2)


# VK
def vk():
    webbrowser.open('https://vk.com/im', new=2)



# МУЗЫКА ВК
def musicVK():
    webbrowser.open('https://vk.com/audios564479476?section=all', new=2)



# ИГРА
def game():
    try:
        webbrowser.open('https://www.supremacy1914.com/game.php?L=14&bust=1#/home/overview/', new=2)
    except:
        voiceBot.speaker('Что то пошло не так')



# ОТКЛЮЧАЕТ БОТА
import  sys
def offBot():
   sys.exit()



# КНИГА
def read():
    try:
        webbrowser.open('https://python.swaroopch.com/control_flow.html', new=2)
    except:
        voiceBot.speaker('Книжка не октрыта')



# ЗАПИСЬ МЫСЛЕЙ
import os
def newText():
    try:
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk")
    except:
        voiceBot.speaker('Путь к файлу не найден, проверьте, правильный ли он')



# ФАЙЛ С ИНФОРМАЦИЕЙ О БОТЕ
def textOpis():

    try:
        os.startfile(r"documentation.txt")
        voiceBot.speaker('открыл')
    except:
        voiceBot.speaker('Путь к файлу не найден, проверьте, правильный ли он')



# ОТКЛЮЧЕНИЕ ПК
def offpc():
    #os.system('shutdown \s')
    print('пк был выключен')



# МОНЕТКА
def monetka():
    r = random.randint(1, 2)
    if r == 1:
        voiceBot.speaker('Выпал орёл')
    elif r == 2:
        voiceBot.speaker('Выпала решка')



# ВРЕМЯ
def time():
    import datetime
    try:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        voiceBot.speaker(f"Сейчас время: {strTime}")
    except:
        voiceBot.speaker('Ошибка со временем')



# ПОГОДА
def weather():#https://openweathermap.org для показывания погоды
    try:
        params = {'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'appid': 'ваш токен'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voiceBot.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
    except:
        voiceBot.speaker('Не опознанная ошибка, проверь API или код')



# ПАССИВНЫЕ ОТВЕТЫ
def passive():#Функция заглушка при простом диалоге с ботом
    pass



# TELEGRAM
def teleg():
    try:
        os.startfile(r"C:\Users\User\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Telegram.lnk")
        voiceBot.speaker('открыл телеграм')
    except:
        voiceBot.speaker('Путь к файлу не найден, проверьте, правильный ли он')






# ФОНОВЫЙ РЕЖИМ
# def sleept():
#     try:
#         voiceBot.speaker("Я вас понял, заглушаюсь")
#         a = int(120)
#         time.sleep(a)
#
#     except:
#         voiceBot.speaker("Пошло что то не так")



# def wikiped():
#     query = callback().lower()
#     try:
#         if 'википедия' in query:
#             voiceBot.speaker('ищу в википедии')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=3)
#             voiceBot.speaker("есть вот такая информация")
#             voiceBot.speaker(results)
#     except:
#         voiceBot.speaker('Нету информации')





# ГУГЛ ПОИСКОВИК
# def siteSearch(task):
#     try:
#         mas = ['сара']
#         keys = ('найди', 'покажи')
#         for i in mas:
#             task = task.replace(i, '')
#             task = task.replace('  ', ' ')
#         task = task.strip()
#
#         for i in keys:
#             if i in task:
#                 zapros = task.replace(i, '')
#                 zapros = zapros.strip()
#                 task = 'найди'
#
#         if task == 'найди':
#             webbrowser.open(f'https://www.google.com/search?q={zapros}&oq=%{zapros}%81&aqs=chrome..69i57j0i131i433i512j0i512l3j46i433i512j0i512l4.1327j0j15&sourceid=chrome&ie=UTF-8')
#
#     except:
#         voiceBot.speaker('Не смог открыть сайт')


# ЮТУБ ПОИСКОВИК
# def search_for_video_on_youtube(*args: tuple):
#     """
#     Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
#     :param args: фраза поискового запроса
#     """
#     if not args[0]: return
#     search_term = " ".join(args[0])
#     url = "https://www.youtube.com/results?search_query=" + search_term
#     webbrowser.get().open(url)




