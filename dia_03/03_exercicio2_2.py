# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas

# Definindo as variáveis

soma = 0    # valor final
numero_input = 4    # contador de entradas

# Recebendo os inputs

for i in range(numero_input):
    altura = input("Insira uma altura: ")
    soma += float(altura)

# Exibindo os resultados

print("Sua soma resultou em:", round(soma, 2))