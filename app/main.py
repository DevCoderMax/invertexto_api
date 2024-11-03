import requests

# URL da requisição
url = "https://www.invertexto.com/ajax/notepad.php"


# Dados a serem enviados no corpo da requisição
data = {
    "saved_text": "test",
    "token": "e83JqSkGeTsyfcjRaDh9KZ5wX0MavnxY"
}

# Enviando a requisição POST
response = requests.post(url, data=data)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Requisição bem-sucedida!")
    print("Conteúdo da resposta:", response.text)
else:
    print("Falha ao acessar a URL:", response.status_code)
