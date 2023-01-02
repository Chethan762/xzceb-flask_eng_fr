"""System module."""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-09-05',
    authenticator=authenticator
)

language_translator.set_service_url('url')

def englishToFrench(englishText):

    frenchText = language_translator.translate(
        text='Hello',
        model_id='en-fr').get_result()

    return frenchText

def frenchToEnglish(frenchText):

    englishText = language_translator.translate(
        text='Bonjour',
        model_id='fr-en').get_result()

    return englishText
