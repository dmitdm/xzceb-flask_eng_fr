from machinetranslation import translator
from flask import Flask, render_template, request
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
url = os.environ['url']
apikey = os.environ['apikey']


# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)



app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    model_id = 'en-fr'
    textToTranslate = language_translator.translate(
    text=textToTranslate,
    model_id=model_id).get_result()
    return textToTranslate.get("translations")[0].get("translation")
    

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    model_id = 'fr-en'
    textToTranslate = language_translator.translate(
    text=textToTranslate,
    model_id=model_id).get_result()
    return  textToTranslate.get("translations")[0].get("translation")

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
