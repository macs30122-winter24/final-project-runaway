import requests, uuid, json

subscription_key = 'key'
endpoint = 'https://api.cognitive.microsofttranslator.com/'
location = 'northcentralus'

# Build the request headers
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# Build the request body
path = '/translate?api-version=3.0'
params = '&from=yue&to=en'  # Translate from Cantonese to English, adjust as needed
constructed_url = endpoint + path + params

# Adjusted list of Cantonese texts with keywords
texts_with_keywords = [
    {"keyword": "特首", "text": "一代特首淪落到咁兜踎"},
    {"keyword": "投票", "text": "投邊個已經無得揀，宜家選擇唔投都無得揀，ok啦咁，我投票你老母!"},
    {"keyword": "政府", "text": "現觀上一輩民主派爭取廿多載可謂一事無成，反觀今次靠年青一代走在最前線卻功效顯著，對現在的政府，只能靠全民不合作運動遍地開花才是唯一上策和出路"},
    {"keyword": "民主", "text": "現觀上一輩民主派爭取廿多載可謂一事無成，反觀今次靠年青一代走在最前線卻功效顯著，對現在的政府，只能靠全民不合作運動遍地開花才是唯一上策和出路"}
]

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
    
    # Save to JSON file with UTF-8 encoding to avoid garbled text
    output_file_path = 'C:/Users/A1157/Downloads/30122 test/translations_with_keywords.json'  # Specify the path and filename
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(translated_texts_with_keywords, f, ensure_ascii=False, indent=4)

    print("Translations saved to JSON file successfully.")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except json.decoder.JSONDecodeError:
    print("Error decoding JSON response")

