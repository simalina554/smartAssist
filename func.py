import webbrowser
import speech_recognition as r
from playsound import *
import pyglet
import datetime

playsound('.\eng.mp3')


def command():
    micro = r.Recognizer()
    # прослушивание микрофона и запись команд в source
    with r.Microphone() as source:
        # прослушивание команды начнется через 1 сек
        micro.pause_threshold = 0.5
        # избавление шума в команде
        micro.adjust_for_ambient_noise(source, duration=1)
        # получение команды
        audio = micro.listen(source)
    # речь -> текст
    try:
        task = micro.recognize_google(audio).lower()
    # если произошла ошибка
    except r.UnknownValueError:
        playsound(r'.\eng1.mp3')
        task = command()
    return task


def make(task):
    if 'open friday' in task:
        url = 'https://friday.ru/live'
        webbrowser.open(url)
    elif 'music' in task:
        music(task)
    elif 'whats day' in task:
        print(datetime.date.today())


def music(task):
    if 'love' in task:
        sound = pyglet.media.load('C:/Users/Alina/Music/Another_Love.mp3', streaming=False)
        sound.play()
        pyglet.app.run()
    elif 'dancing' in task:
        sound = pyglet.media.load(r'C:\Users\Alina\Music\Dancin.mp3', streaming=False)
        sound.play()
        pyglet.app.run()
    elif 'time out' in task:
        sound = pyglet.media.load(r'C:\Users\Alina\Music\Tajmaut.mp3', streaming=False)
        sound.play()
        pyglet.app.run()


while True:
    make(command())
