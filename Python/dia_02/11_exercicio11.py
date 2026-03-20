# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

#%%
#Recebendo o input "item"
item = input("Insira o item desejado: ")
item = item.lower()
#Verificando se pertence a lista de compras
lista = ["laranja", "cerveja", "miojo", "carvão", "picanha"]
verdade = ""
if item in lista:
    print("Está na lista de compras!")
else:
    print("Não comprar")