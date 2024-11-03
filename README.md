Invertexto API (Unofficial)

## Task List

This section outlines the planned and ongoing tasks for the API.

- [x] **Notepad Creation**
- [x] **Get Content**
- [x] **Set Content**

## Exemplos de Uso

#instalação da biblioteca
```python
pip install git+https://github.com/DevCoderMax/invertexto_api.git
```
#Uso
```python
# cria um notepad
from invertexto_api.modules import Notepad
notepad = Notepad("max")
print(notepad.create())
pega o conteudo do notepad
notepad = Notepad("max")
print(notepad.get_content())
seta o conteudo do notepad
notepad = Notepad("max")
print(notepad.set_content("testing", 'token')) 
```

