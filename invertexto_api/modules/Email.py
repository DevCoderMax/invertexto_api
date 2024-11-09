import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

class Email:
    def __init__(self):
        self._base_url = "https://www.invertexto.com/gerador-email-temporario?email="
        self._end_url = "@uorak.com"

    def generate_email():
        page = requests.get("https://www.invertexto.com/gerador-email-temporario").content
        soup = BeautifulSoup(page, 'html.parser') 
        email = soup.find(id='email-input') 
        return email.get('value') 

    def create_custom_email(username):
    
        url = "https://www.invertexto.com/gerador-email-temporario?email="
        end_url = "@uorak.com"
        url_final = url+username+end_url
        email = username+end_url
        response = requests.get(url_final)

        if email in response.text:
            return True
        else:
            return False
        
