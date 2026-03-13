# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas

# Definindo as variáveis

soma = 0    # valor final

numero_input = 4    # contador de entradas

count = 1   # contador sequencial

# Recebendo os inputs

while count <= numero_input:
    altura = float(input("Digite aqui uma altura:"))
    soma += altura
    count += 1

# Exibindo os resultados

print("Sua soma resultou em:", soma)