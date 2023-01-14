from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(englishText):
    
    frenchText = language_translator.translate(
        text='Hello',
        model_id='en-fr'
        ).get_result()

    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text='Bonjour',
        model_id='fr-en'
        ).get_result()

    return englishText

@app.route("/")
def renderIndexPage():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
