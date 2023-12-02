#1
def es_par (n: int) -> bool:
    res = False
    if n % 2 == 0 : res = True

    return res
    
#2
def dos_pertenece(lista : list) -> bool:
    for i in lista:
        if i == 2: return True 
    return False
    
#3
def pertenece():
    return

#4
def mas_larga(l1: list[int], L2: list[int])-> list[int]:
    res = l1
    if l1.__len__() > L2.__len__() : l1
    else: res = L2
    return res
 
#5
def cant_e(lista : list[str]) -> int:
    res = 0
    for i in lista:
        if i == 'e' : res+=1
    return res
 
#6
def sumar_unos(lista : list [int]) -> list [int]:
    for i in range(0,lista.__len__()): lista[i] +=1
    return lista

#7
def mezclar(c1: str, c2: str)-> str:
    
    return

#Extras
def es_primo(): #devuelve true o false si el n dado es primo o no
    return

#FACTORIAL: 3!=1*2*3=6, 0!=1
def factorial_ite(): #devuelve el factorial de un numero de forma iterada
    return

def factorial_recu(): #mismo que el anterior pero usando recursion
    return

def matriz_por_escalar(): #multiplica cada elemento de una matriz por n
    return

def suma_gauss(): #suma todos los nuemeros hasta el n dado
    return

def geringoso(): # recibe una palabra y la convierte en geringoso -> voto->vopotopo
    return