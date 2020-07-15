#This project take text or article and convert them into speech...

#Import some libary

from newspaper import Article
import nltk
from gtts import gTTS
import os

#grt the article from online
article=Article("http://pradhyumnasinghrathore.live/")

article.download()#article download
article.parse()#parse the article
nltk.download('punkt')#download the punkt package
article.nlp() #natural learning processing

#get the article text and store in variable

mytext=article.text

#print the text
print(mytext)

#selecting language for speech normally we going to select english
language='en'

#convert text_To_speech
myobj=gTTS(text=mytext,lang=language,slow=False)

#save the converted audio to file
myobj.save('read_article.mp3')

#play that file
os.system('start read_article.mp3')