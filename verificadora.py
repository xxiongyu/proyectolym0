
from nltk.tokenize import sent_tokenize, word_tokenize
archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
list = word_tokenize(text)
print(word_tokenize(text))

