
from nltk.tokenize import sent_tokenize, word_tokenize
archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
lista_word = word_tokenize(text)
size = len(lista_word)
dicc = {}
for a in range(0,size):
    b = a+1
    c = a+2
    word = lista_word[a]
    if word == 'defVar':
        variable = lista_word[b]
        valor = lista_word[c]
        dicc[variable] = valor
    
    if word == 'defProc':
        variable = lista_word[b]
        
#print(lista_word)

