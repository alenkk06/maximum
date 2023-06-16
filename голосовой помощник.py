from gtts import gTTS
from pygame import mixer
from time import sleep

mp3_name = 'test_1.mp3'
txt = 'привет,серёга!'

mixer.init()

mp3 = gTTS(text=txt, lang = 'ru')
mp3.save(mp3_name)
mixer.music.load(mp3_name)
mixer.music.play()
sleep(5)
