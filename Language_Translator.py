from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from pandas import json_normalize

from Watson_Speech_to_Text_Translator import recognized_text

url_lt = 'insert url here'
apikey_lt = 'insert api key here'

version_lt = '2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-pt')
translation_response

translation = translation_response.get_result()
translation

spanish_translation = translation['translations'][0]['translation']
print(spanish_translation)
