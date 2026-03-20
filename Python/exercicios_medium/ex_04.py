#%%
# Utilize while para permitir o usuário fazer contas de adição enquanto quiser.

print("Bem vindo à operação de - Adição")

numero_01 = input ("Insira o primeiro número aqui: ")
numero_02 = input ("Insira o segundo número aqui: ")
soma = float(numero_01) + float(numero_02)
print("O resultado é: ", round(soma))

resposta = input ("Deseja continuar? (S) / (N): ")

while resposta.lower() == "s":
    numero_01 = input ("Insira o primeiro número aqui: ")
    numero_02 = input ("Insira o segundo número aqui: ")
    soma = float(numero_01) + float(numero_02)
    print("O resultado é: ", round(soma, 2))
    resposta = input ("Deseja continuar? (S) / (N): ")

print("Exercício finalizado.")