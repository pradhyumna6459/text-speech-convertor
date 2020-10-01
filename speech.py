#This project take text or article and convert them into speech...
#Import some libary

from newspaper import Article
from gtts import gTTS
from playsound import playsound
import time

start = time.time()
#get the article from online
article=Article("http://pradhyumnasinghrathore.live/")
article.download()

#parse the article
article.parse()
mytext=article.text

#selecting language for speech normally we going to select english
language='en'

#convert text_To_speech
myobj=gTTS(text=mytext,lang=language,slow=False)

#save the converted audio to file
myobj.save('read_article.mp3')

#play that file
playsound('read_article.mp3')
print(time.time()-start)