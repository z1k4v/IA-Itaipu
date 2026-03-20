# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:
#	O número x é impar
#ou
#	O número x é par

#%%
numero = input("Insira um número inteiro aqui: ")
if int(numero) % 2 == 0:
    print("O número", numero, "é par")
else:
    print("O número", numero, "é impar")