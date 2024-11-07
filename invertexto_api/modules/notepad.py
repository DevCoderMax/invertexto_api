import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional

class Notepad:
    """
    Classe para interagir com o serviço de notepad do Invertexto.
    Permite criar, ler e atualizar notas de texto.
    """
    
    BASE_URL = "https://www.invertexto.com"
    
    def __init__(self, username: str):
        """
        Inicializa um novo notepad.
        
        Args:
            username (str): Nome de usuário para identificar o notepad
        """
        self.username = username
    
    def create(self) -> Dict:
        """
        Cria um novo notepad.
        
        Returns:
            Dict: Resposta da API contendo status da criação
        """
        url = f"{self.BASE_URL}/ajax/notepad-create.php"
        data = {"username": self.username}

        response = requests.post(url, data=data)
        return response.json()
    
    def get_content(self) -> Dict:
        """
        Obtém o conteúdo atual do notepad, incluindo token de edição.
        
        Returns:
            Dict: Dicionário contendo conteúdo, user_id e token de edição
        """
        url = f"{self.BASE_URL}/{self.username}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Localiza o textarea com o conteúdo e o script com dados de autenticação
        textarea = soup.find('textarea')
        script = soup.find('script', text=lambda t: t and 'function run()' in t)
        
        if textarea is None:
            return {"error": "Notepad não encontrado"}
            
        # Extrai user_id e token do script JavaScript
        user_id, token = self._extract_auth_data(script)
        
        return {
            "content": textarea.text if textarea.text else "Notepad está vazio",
            "user_id": user_id,
            "token": token
        }
    
    def _extract_auth_data(self, script) -> tuple[Optional[str], Optional[str]]:
        """
        Extrai dados de autenticação do script JavaScript.
        
        Args:
            script: Elemento script contendo os dados
            
        Returns:
            tuple: (user_id, token)
        """
        script_text = script.string if script else ""
        user_id = None
        token = None
        
        if script_text:
            for line in script_text.split('\n'):
                if "userId =" in line:
                    user_id = line.split("'")[1]
                elif "token =" in line:
                    token = line.split("'")[1]
                    
        return user_id, token
    
    def set_content(self, content: str, token: str) -> Dict:
        """
        Atualiza o conteúdo do notepad.
        
        Args:
            content (str): Novo conteúdo do notepad
            token (str): Token de autenticação obtido via get_content()
            
        Returns:
            Dict: Resposta da API confirmando a atualização
        """
        url = f"{self.BASE_URL}/ajax/notepad.php"
        data = {
            "username": self.username,
            "saved_text": content,
            "token": token
        }
        response = requests.post(url, data=data)
        return response.json()
