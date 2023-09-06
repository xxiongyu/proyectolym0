
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
            v_publico = dicc_publico.keys()
            v_privado = dicc_privado.get(variable)
            verificacion = 0 
            list_rango = str(list(range(1,100))) 
            posiciones = ["x","y","v"]
            list_posicion = ['right','left','front','back'] 
            list_cardinales =['north','south','west','east'] 
            list_commansTurn = ['left','right','around']  
            lista_comandos = ['jump','walk','leap','turn','turnto','drop','get','grab','letGo','nop']  
            if coordenada_complititud == -1000:
                print('False')
            else:

                for bb in range(llavedefuncion, coordenada_complititud):
                    if word == 'jump': 
                        b = a+1 
                        indesado = lista_word.index(')',b)  
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and (lista_word[aa+2] in list_rango or lista_word[aa+2] in posiciones):  
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'walk': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_posicion: 
                                    verificacion+0
                            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_cardinales: 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'leap': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_posicion: 
                                verificacion+0
                            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_cardinales: 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'turn': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_commansTurn): 
                                verificacion+0
                            else:
                                verificacion+1
                    if word =='turnto': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_cardinales):
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'drop': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'get': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'grab': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'letGo': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'nop':    
                        b = a+1 
                        c = a+2
                        if b == '(' and c == ')': 
                            verificacion+0
                        else:
                            verificacion+1            
                    if word == 'facing': 
                        b = a+1 
                        indensado = lista_word.index(')',b) 
                        for aa in range(b+1,indensado): 
                            if lista_word[aa] in list_cardinales: 
                                verificacion+0
                            else:
                                verificacion+1
                    if word == 'can': 
                        b = a+1 
                        indendado = lista_word.index(')',b)      
                        for aa in range(b+1,indendado): 
                            if lista_word[aa] in lista_comandos: 
                                verificacion+0
                            else:
                                verificacion+1
                    if  word == 'not': 
                        b = a+1 
                        condicion = lista_word[b] 
                        if condicion == 'can' or condicion == 'facing': 
                            verificacion+0
                        else:
                            verificacion+1
            if verificacion > 1:
                print('False')    
            



    
        
            



