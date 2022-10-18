# Ejercicio 1 #
'''
Realizar un programa que inicialice una lista con 10 valores aleatorios
(del 1 al 10) y posteriormente muestre en pantalla cada
elemento de la lista junto con su cuadrado y su cubo.
'''
import random

def lista_numeros():
    contador = 0
    lst=[]
    while(contador<10):
        num_random=random.randint(1,10)
        contador+=1
        lst.append(num_random)
    return lst

lista = lista_numeros()
print(lista)
def lista_cuadrado(lst):
    lst_cuadrado=[]
    for i in lst:
        num_cuadrado= i*i
        lst_cuadrado.append(num_cuadrado)
        num_cuadrado=0
    return lst_cuadrado

print(lista_cuadrado(lista))

def lista_cubo(lst):
    lst_cubo=[]
    for i in lst:
        num_cubo= i*i*i
        lst_cubo.append(num_cubo)
        num_cubo=0
    return lst_cubo
print(lista_cubo(lista))
