from flask import Flask, render_template, request, redirect
from newspaper import Article
from gtts import gTTS
from playsound import playsound
import os

app = Flask(__name__)
count = 0

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/trigger", methods=["POST"])
def trigger():
	if request.form.get("texttospeech") != "":
		text = request.form.get("texttospeech")
		print("this is running")
	else:
		url = request.form.get('articleurl')
		article=Article(url)
		article.download()
		article.parse()
		text=article.text

	tts = gTTS(text, lang='en')
	global count
	tts.save(str(count)+'.mp3')
	playsound(str(count)+'.mp3')
	count += 1
	return render_template("base.html")


if __name__ == "__main__":
	app.run(debug=True)