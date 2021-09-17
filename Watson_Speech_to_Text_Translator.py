from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/4ba23cc7-a027-461b-9614-de4781b665d5"
iam_apikey_s2t = "_LJ0JQ0PmjeoDn83oh-06wFWvvUqV-IIFR4UXqn-DhA1"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

filename = 'PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb") as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

response.result

json_normalize((response.result['results'], 'alternatives'))
response

recognized_text = response.result['results'][0]['alternatives'][0]['transcript']
type(recognized_text)
print(response)
