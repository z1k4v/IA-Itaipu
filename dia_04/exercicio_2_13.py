# Faça um programa que receba um número e exiba seu fatorial.

#%%
fatorial = 1
numero = input("Insira um número inteiro: ")
numero = int(numero)
for i in range(1, numero +1):
    fatorial *= i
print (fatorial)