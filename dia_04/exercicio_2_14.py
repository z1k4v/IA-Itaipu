# Considere a seguinte lista:
#  [123, 435, 987, 1984, 2, 19, 423, -178, 320]
# Faça um programa que retorne a posição do menor e do maior valor encontrado:

#%%
lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]
maior = lista[0]
menor = lista[0]
posicaomaior = 0
posicaomenor = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posicaomaior = i
    if lista[i] < menor:
        menor = lista[i]
        posicaomenor = i

print(posicaomaior)
print(posicaomenor)