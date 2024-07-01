import requests

def get_quote():
    api_url = f'https://zenquotes.io/api/random/keyword=success'
    data = requests.get(api_url).json()
    text = data[0]['q']
    author = data[0]['a']
    #Returns dict containing quote and author
    quote = {'quote': text, 'author': author}

    return quote