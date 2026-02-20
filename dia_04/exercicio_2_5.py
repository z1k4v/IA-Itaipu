# Considere a lista: [120, “Python”, 120.01, “asw”, False, [10,20] ]
#   Faça um programa que retorne as seguintes informações:
#       Elemento na posição -1 da lista
#       Elemento na primeira posição da lista
#       O último caractere do segundo elemento da lista
#%%
lista = [120, "Python", 120.01, "asw", False, [10,20]]
print(lista[-1])
print(lista[0])
lista2 = list(lista[1])
print(lista2[-1])