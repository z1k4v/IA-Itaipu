# Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...
# Exiba o número da sequência cuja posição foi informada:

#%%
posicao = input("Insira aqui a posição desejada: ")
cont = 3
proximo = ""
fibonacci = [0, 1]
while cont <= int(posicao):
    proximo = fibonacci [-1] + fibonacci [-2]
    fibonacci.append(proximo)
    cont += 1
print(fibonacci[-1])