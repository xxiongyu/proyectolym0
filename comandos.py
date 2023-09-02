import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
nltk.download("punkt")
archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
lista_word = word_tokenize(text)
size = len(lista_word) 
verificacion = 0 
mensaje = False
list_rango = list(range(1,100)) 
list_posicion = ['right','left','front','back'] 
list_cardinales =['north','south','west','east'] 
list_commansTurn = ['left','right','around']
dicc = {}
for a in range(0,size):
    b = a+1
    c = a+2
    word = lista_word[a]
    if word == 'defVar':
        variable = lista_word[b]
        valor = lista_word[c]
        dicc[variable] = valor
#verificacion comandos simples    
    if word == 'defProc':
        variable = lista_word[b]  
    if word == 'jump' and word+1 == '(' and word+2 in list_rango  and word+3 == ',' and word+4 in list_rango and word+5 == ')': 
        verificacion += 1 
    if word == 'walk' and word+1 == '(' and word+2 in list_rango  and word+3 == ')': 
        verificacion +=1 
    elif word == 'walk' and word+1 == '(' and word+2 in list_rango and  word+3 in list_posicion  and word+4 == ')':  
        verificacion +=1 
    elif word == 'walk' and word+1 == '(' and word+2 in list_rango and  word+3 in list_cardinales  and word+4 == ')': 
        verificacion +=1 
    if word == 'leap' and word+1 == '(' and word+2 in list_rango and word+3 == ')': 
        verificacion +=1 
    elif word == 'leap' and word+1 == '(' and word+2 in list_rango and word+3 == ',' and word+4 in  list_posicion and word+5 ==')': 
        verificacion +=1 
    elif word == 'leap' and word+1 == '(' and word+2 in list_rango and word+3 == ',' and word+4 in  list_cardinales and word+5 ==')':  
        verificacion +=1 
    if word == 'turn' and word+1 =='(' and word+2 in list_commansTurn and word+3 == ')': 
        verificacion +=1 
    if word == 'turnto' and word+1 == '(' and word+2 in list_cardinales and word+3 == ')': 
        verificacion +=1 
    if word == 'drop' and word+1 == '(' and word+2 in list_rango and word+3 == ')': 
        verificacion +=1  
    if word =='get' and word+1 == '('  and word+2 in list_rango and word+3 == ')': 
        verificacion +=1 
    if word == 'grab' and word+1 == '(' and word+2 in list_rango and word+3 == ')': 
        verificacion +=1 
    if word == 'letGo' and word+1 == '(' and word+2 in list_rango and word+3 == ')': 
        verificacion +=1 
    if word == 'nop' and word+1 =='(' and word+2 == ')': 
        verificacion +=1   
#verificacion de condicionales HACER 
if verificacion > 1 : 
    mensaje = True    
     


