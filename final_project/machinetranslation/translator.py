import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)
language_translator

def englishToFrench(englishText):
    if (englishText==""):
        return englishText
    else:
        French_translation=language_translator.translate(
        text=englishText , model_id='en-fr').get_result()
        frenchText = French_translation['translations'][0]['translation'] 
        return frenchText

def frenchToEnglish(frenchText):
    if (frenchText==""):
        return frenchText
    else:
        English_translation=language_translator.translate(text=frenchText ,model_id='fr-en').get_result()
        englishText = English_translation['translations'][0]['translation']
        return englishText

 