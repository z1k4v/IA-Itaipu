# Faça um programa que receba uma quantidade indefinida de valores correspondentes a "saldo em conta",
#   mas quando o usuário apertar "enter" sem digitar valor algum, o programa para de receber valores,
#   e exibe a soma de todos os valores digitados anteriormente.

# Definindo as variáveis

soma = 0    # vai armazenar o saldo a cada digitação

count = 1   # contador sequencial

saldo = 0

# Registrando saldos a adicionar

while True:
    saldo = input("Insira o saldo a adicionar: ")
    if saldo == "":
        break
    soma += float(saldo)

# Exibindo resultados

print("Seu saldo total é de: ", round(soma, 2))