# Faça um programa com uma função que recebe uma frase. Para cada palavra nesta frase, inverta a ordem das letras. Exiba o resultado:

#%%
frase = input("Digite aqui a sua frase: ")
inverso = ""

for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]

print(frase)

print(inverso)