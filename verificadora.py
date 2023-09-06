
from nltk.tokenize import word_tokenize
#archivo = input('ingrese el arhivo: ')
archivo = 'ejemploFull.txt'
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
lista_word = word_tokenize(text)
size = len(lista_word)
dicc_publico = {}
dicc_privado = {}

def RevisionCompletitud(list, index, qc, Findex):
    print(qc)
    print(index)
    print('-----------------')
    if qc < -1:
        return -1000
    elif qc == 0:
        return Findex
    else:
        if list[index]== '{':
            RevisionCompletitud(list, index+1, qc+1, Findex)
        elif list[index] == 'defProc':
            RevisionCompletitud(list, index+1, -10, Findex)
        elif list[index] == '}' and qc>1:
            RevisionCompletitud(list, index+1, qc-1, Findex)
        elif list[index] != '{' and list[index] != '}':
            RevisionCompletitud(list, index+1, qc, Findex)
        
        else:
            RevisionCompletitud(list, index, qc-1, index)

for a in range(0,size):
    word = lista_word[a]
    if word == 'defVar':
        b = a+1
        c = a+2
        variable = lista_word[b]
        valor = lista_word[c]
        dicc_publico[variable] = valor
    
    if word == 'defProc':
        b = a+1
        c = a+2
        lista = []
        variable = lista_word[b]
        indesado = lista_word.index(')', c)
        for aa in range(c+1,indesado):
            if lista_word[aa] != ',':
                lista.append(lista_word[aa])
        dicc_privado[variable]=lista
        llavedefuncion = indesado+1
        if lista_word[llavedefuncion] == '{':
            indesadofuncion = lista_word.index('}',llavedefuncion)
            coordenada_complititud = RevisionCompletitud(lista_word, llavedefuncion, 1, 0)
            for bb in range(llavedefuncion, coordenada_complititud):
                v_publico = dicc_publico.keys()
                v_privado = dicc_privado.get(variable)
                



    
        
            



