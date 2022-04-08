from gtts import gTTS
from playsound import playsound

# запись и чтение файла mp3
text = "Hey, I'm Hope. What you want? Call the team!"
# эти функции записывают текст в файл
rt = gTTS(text=text, lang='en')
rt.save('eng.mp3')


# если будет ошибка
under = "I'm sorry, but i don't understand you"
stand = gTTS(text=under, lang='en')
stand.save('eng1.mp3')