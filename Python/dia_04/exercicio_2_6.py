# Escreva um programa que solicite ao usuário duas strings e as concatene em uma única String. Em seguida, exiba a String resultante.

#%%
palavra1 = input("Insira uma palavra: ")
palavra2 = input("Insira uma nova palavra: ")
lista = [palavra1, palavra2]
resultado = ""
resultado = resultado.join(lista)
print(resultado)