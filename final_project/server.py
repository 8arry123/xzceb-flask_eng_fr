from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    translation = language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translation'][0]['translation']
    return french_text

@app.route("/frenchToEnglish")
def french_to_english(french_text):
    translation = language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    english_text=translation['translation'][0]['translation']
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
