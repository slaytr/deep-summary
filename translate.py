import six
import os
from google.cloud import translate_v2 as translate
print(os.environ)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\Slayt\\Documents\\GoogleCloudPlatformKeys\\deep-summary-service-account.json'

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


text = "The above code creates a new React component called HelloMessage. This component takes an argument called name which is then passed down to the HTML where it is used as the value for the Hello variable."
target = "mi"

translate_text(target, text)