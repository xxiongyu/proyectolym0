import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
nltk.download("punkt")
archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
lista_word = word_tokenize(text)
size = len(lista_word) 
verificacion = False 
list_rango = str(list(range(1,100)) )
list_posicion = ['right','left','front','back'] 
list_cardinales =['north','south','west','east'] 
list_commansTurn = ['left','right','around']
dicc = {} 
def cod_verification (size):
    for a in range(0,size):
        b = a+1
        c = a+2 
        d = a+3
        e = a+4
        f = a+5
        word = lista_word[a] 
        word1 = lista_word[b] 
        word2 = lista_word[c] 
        word3 = lista_word[d] 
        word4 = lista_word[e] 
        word5 = lista_word[f]
#verificacion comandos simples    
        if word == 'jump' and word1== '(' and word2 in list_rango  and word3 == ',' and word4 in list_rango and word5 == ')': 
            verificacion = True 
        if word == 'walk' and word1 == '(' and word2 in list_rango  and word3 == ')': 
            verificacion = True
        elif word == 'walk' and word1 == '(' and word2 in list_rango and  word3 in list_posicion  and word4 == ')':  
            verificacion = True
        elif word == 'walk' and word1 == '(' and word2 in list_rango and  word3 in list_cardinales  and word4 == ')': 
            verificacion = True
        if word == 'leap' and word1 == '(' and word2 in list_rango and word3 == ')': 
            verificacion = True
        elif word == 'leap' and word1 == '(' and word2 in list_rango and word3 == ',' and word4 in  list_posicion and word5 ==')': 
            verificacion = True 
        elif word == 'leap' and word1 == '(' and word2 in list_rango and word3 == ',' and word4 in  list_cardinales and word5 ==')':  
            verificacion = True
        if word == 'turn' and word1 =='(' and word2 in list_commansTurn and word3 == ')': 
            verificacion = True 
        if word == 'turnto' and word1 == '(' and word2 in list_cardinales and word3 == ')': 
            verificacion = True 
        if word == 'drop' and word1 == '(' and word2 in list_rango and word3 == ')': 
            verificacion = True  
        if word =='get' and word1 == '('  and word2 in list_rango and word3 == ')': 
            verificacion = True 
        if word == 'grab' and word1 == '(' and word2 in list_rango and word3 == ')': 
            verificacion = True 
        if word == 'letGo' and word1 == '(' and word2 in list_rango and word3 == ')': 
            verificacion = True
        if word == 'nop' and word1 =='(' and word2 == ')': 
            verificacion = True    
    return verificacion 
        


