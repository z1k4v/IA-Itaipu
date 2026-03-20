# Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:

#%%
numero = int(input("Insira aqui um número: "))
if numero <= 1:
        print("O número", numero, "não é primo")
elif numero == 2:
        print("O número", numero, "é primo")
elif numero % 2 == 0:
        print("O número", numero, "não é primo")
else:
    for i in range (3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            print("O número", numero, "não é primo")
            break
    else:
            print("O número", numero, "é primo")