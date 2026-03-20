#Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista

#%%
#Definições
lista = [1,2,5,5,1,2,8,6,5,4,2,54,4,2,475,5,8,54,75,9,4,1,1,2,5,75,5,54,1,54,5,4,14,4,1,7,3,8,9,65,4]
numero = input("Insira aqui um número: ")
contagem = 0
#Varredura de lista
for i in lista:
    if i == int(numero):
        contagem += 1
#Resultado
print("Quantidade de", numero, "=", contagem)