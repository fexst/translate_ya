import requests

word = 'requests'
url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'your_api_token_here'  # Replace this with your actual API token
params = {
    'key': token,
    'lang': "en-ru",  # 'en-ru' means translating from English to Russian
    'text': word
}

response = requests.get(url, params=params)  # Make the GET request
if response.status_code == 200:  # Check if the request was successful
    # Extract translation from the JSON response
    translation = response.json()['def'][0]['tr'][0]['text']
    print(f'Translation of "{word}": {translation}')
else:
    print(f'Error: Unable to fetch data. Status code: {response.status_code}')
