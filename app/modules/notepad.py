import requests
from bs4 import BeautifulSoup

class Notepad:
    def __init__(self, username: str):
        self.username = username
    
    def create(self):
        url = "https://www.invertexto.com/ajax/notepad-create.php"
        data = {
            "username": self.username,
        }

        response = requests.post(url, data=data)
        return response.json()
    
    def get_content(self):
        url = "https://www.invertexto.com/"
        data = {
            "username": self.username,
        }
        end_url = url + self.username
        response = requests.get(end_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra o textarea e o script com as informações
        textarea = soup.find('textarea')
        script = soup.find('script', text=lambda t: t and 'function run()' in t)
        
        if textarea is None:
            return {"error": "Notepad not found"}
            
        # Extrai as informações do script
        script_text = script.string if script else ""
        user_id = None
        token = None
        
        if script_text:
            for line in script_text.split('\n'):
                if "userId =" in line:
                    user_id = line.split("'")[1]
                elif "token =" in line:
                    token = line.split("'")[1]
        
        return {
            "content": textarea.text if textarea.text else "Notepad is empty",
            "user_id": user_id,
            "token": token
        }
    
    def set_content(self, content: str, token: str):
        url = "https://www.invertexto.com/ajax/notepad.php"
        data = {
            "username": self.username,
            "saved_text": content,
            "token": token
        }
        response = requests.post(url, data=data)
        return response.json()
