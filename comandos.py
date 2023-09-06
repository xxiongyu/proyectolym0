import nltk
from nltk.tokenize import  word_tokenize 
nltk.download("punkt")
archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
lista_word = word_tokenize(text) 
size = len(lista_word) 
verificacion = 0 
list_rango = str(list(range(1,100))) 
posiciones = ["x","y","v"]
list_posicion = ['right','left','front','back'] 
list_cardinales =['north','south','west','east'] 
list_commansTurn = ['left','right','around']  
lista_comandos = ['jump','walk','leap','turn','turnto','drop','get','grab','letGo','nop']  
for a in range(0,size):
    word = lista_word[a]     
    if word == 'jump': 
        b = a+1 
        indesado = lista_word.index(')',b)  
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and (lista_word[aa+2] in list_rango or lista_word[aa+2] in posiciones):  
                verificacion 
    if word == 'walk': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                verificacion 
            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_posicion: 
                    verificacion
            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_cardinales: 
                verificacion 
    if word == 'leap': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                verificacion 
            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_posicion: 
                verificacion
            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_cardinales: 
                verificacion 
    if word == 'turn': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_commansTurn): 
                verificacion 
    if word =='turnto': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_cardinales):
                verificacion 
    if word == 'drop': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                verificacion 
    if word == 'get': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                verificacion 
    if word == 'grab': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                verificacion 
    if word == 'letGo': 
        b = a+1 
        indesado = lista_word.index(')',b) 
        for aa in range(b+1,indesado): 
            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                verificacion 
    if word == 'nop':    
        b = a+1 
        c = a+2
        if b == '(' and c == ')': 
            verificacion  
    #adelantar condicionales                
    if word == 'facing': 
        b = a+1 
        indensado = lista_word.index(')',b) 
        for aa in range(b+1,indensado): 
            if lista_word[aa] in list_cardinales: 
                verificacion 
    if word == 'can': 
        b = a+1 
        indendado = lista_word.index(')',b)      
        for aa in range(b+1,indendado): 
            if lista_word[aa] in lista_comandos: 
                verificacion 
    if  word == 'not': 
        b = a+1 
        condicion = lista_word[b] 
        if condicion == 'can' or condicion == 'facing': 
            verificacion 
    print (verificacion)
    
        

            
        


