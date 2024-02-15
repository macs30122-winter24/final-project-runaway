import requests, uuid, json

# 设置你的密钥和端点
subscription_key = '27821efaf9b1401c886547be7b6898bd'
endpoint = 'https://api.cognitive.microsofttranslator.com'
location = 'northcentralus'

# 构建请求头部
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# 构建请求体
path = '/translate?api-version=3.0'
params = '&from=yue&to=en'  # 从粤语翻译到英语，根据需要调整
constructed_url = endpoint + path + params

# 粤语文本示例
body = [{
    'text': '粤语文本示例'
}]

# 发送请求并获取响应
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, indent=4, ensure_ascii=False))

