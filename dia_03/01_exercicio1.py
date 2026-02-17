# Faça um programa que conte quantas vezes a letra "a" aparece em uma palavra

# %%

# Definindo a letra

qtd_letra = 0

# Pedindo a inserção da palavra

palavra = input("Digite aqui uma palavra qualquer: ")

# Contando quantas vezes a letra "a" foi inserida

for i in palavra:
    if i == "a":
        i = 1
        qtd_letra = qtd_letra + i

print("O resultado é :", qtd_letra)