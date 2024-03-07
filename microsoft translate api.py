import requests
import uuid
import json

def translate_text(input_file_path, output_file_path, subscription_key, endpoint='https://api.cognitive.microsofttranslator.com/', location='northcentralus'):
    """
    Translates text from Cantonese to English using Microsoft's Cognitive Services Translator.

    :param input_file_path: The file path to the input JSON file containing texts with keywords.
    :param output_file_path: The file path where the translated texts with keywords should be saved.
    :param subscription_key: The subscription key for Microsoft's Cognitive Services Translator.
    :param endpoint: The endpoint URL for the translation service.
    :param location: The location for the translation service, should be same as the one used while setting up the service.

    :return: None
    """

    # Build the request headers
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Build the request body
    path = '/translate?api-version=3.0'
    params = '&from=yue&to=en'  # Translate from Cantonese to English
    constructed_url = endpoint + path + params

    # Load texts with keywords from input file
    with open(input_file_path, 'r', encoding='utf-8') as f:
        texts_with_keywords = json.load(f)

    # Prepare texts for translation
    texts_for_translation = [{"text": item["text"]} for item in texts_with_keywords]

    # Attempt to send the request and get the response
    try:
        response = requests.post(constructed_url, headers=headers, json=texts_for_translation)
        response.raise_for_status()  # Raises an exception if the response status code is not 200
        translations = response.json()

        # Extract translated texts and include keywords
        translated_texts_with_keywords = [
            {"Keyword": item["keyword"], "Original Text": item["text"], "Translated Text": translation['translations'][0]['text']}
            for item, translation in zip(texts_with_keywords, translations)
        ]
        
        # Save
