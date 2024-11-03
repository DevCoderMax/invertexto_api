
from app.modules.notepad import Notepad

#exemplo de uso

#cria um notepad
notepad = Notepad("max")
print(notepad.create())

#pega o conteudo do notepad
notepad = Notepad("max")
print(notepad.get_content())

#seta o conteudo do notepad
notepad = Notepad("max")
print(notepad.set_content("testing", 'token'))