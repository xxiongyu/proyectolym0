
from nltk.tokenize import sent_tokenize, word_tokenize
import funciones
#archivo = input('ingrese el arhivo: ')
archivo = 'ejemploFull.txt'
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
lista_word = word_tokenize(text)
size = len(lista_word)
dicc = {}
print(lista_word[243],lista_word[244],lista_word[245],lista_word[246])

def RevisionCompletitud(llavedefuncion, indesadofuncion, lista):
    originalindesado = indesadofuncion
    sentinela = None
    indesadofuncion = indesadofuncion
    vigilante = 0
    for aa in range(llavedefuncion+1,indesadofuncion):
        if lista[aa] == '{':
            sentinela = indesadofuncion
            indesadofuncion = lista.index('}',sentinela+1)
            vigilante += 1
            print(indesadofuncion)
    if vigilante >= 1:
        RevisionCompletitud(sentinela+1, indesadofuncion, lista)
    if vigilante == 0:
        return originalindesado


for a in range(0,size):
    word = lista_word[a]
    if word == 'defVar':
        b = a+1
        c = a+2
        variable = lista_word[b]
        valor = lista_word[c]
        dicc[variable] = valor
    
    if word == 'defProc':
        b = a+1
        c = a+2
        lista = []
        variable = lista_word[b]
        indesado = lista_word.index(')', c)
        for aa in range(c+1,indesado):
            if lista_word[aa] != ',':
                lista.append(lista_word[aa])
        dicc[variable]=lista
        llavedefuncion = indesado+1
        if lista_word[llavedefuncion] == '{':
            indesadofuncion = lista_word.index('}',llavedefuncion)
            coordenada_complititud = RevisionCompletitud(llavedefuncion, indesadofuncion, lista_word)
            print(coordenada_complititud)
            for bb in range(llavedefuncion, coordenada_complititud):
                valores = dicc.get(variable)
                print(valores)




    
        
            

#print(lista_word)

