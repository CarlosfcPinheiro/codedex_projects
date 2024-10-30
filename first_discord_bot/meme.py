# Importing libraries/packages
# requests => To make http requests
# json => Manage json format
import requests
import json

# CCreating class meme
class Meme:
    # Static method to call method get_meme
    @staticmethod
    def get_meme() -> dict:
        response = requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        return json_data['url']
    
