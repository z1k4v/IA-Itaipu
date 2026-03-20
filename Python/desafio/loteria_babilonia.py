#Construa um programa que realiza o sorteio de um número entre 1 e 15.
#O usuário terá 3 chances de acertar o valor.
#A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
#Caso o usuário acerte, dê os parabéns.

#%%
import random

def get_input():
    while True:
        try:
            palpite = int(input("Insira aqui seu palpite de 1 a 15: "))
        except ValueError as err:
            print("Valor inválido.")
            continue
        if 1 <= palpite <= 15:
            return palpite
        print("Valor inválido. Deve estar entre 1 e 15.")

def check_palpites(numero_sorteio, palpite):
    if numero_sorteio == palpite:
        print("Parabéns, você acertou!")
        return True
    elif numero_sorteio > palpite:
        print("Palpite menor que o sorteado")
        return False
    else:
        print("Palpite maior que o sorteado")
        return False

numero_sorteio = random.randint(1,15)
for i in range(3):
    palpite = get_input()
    if check_palpites(numero_sorteio=numero_sorteio, palpite=palpite):
        break
    
else:
    print("Lamento, não foi dessa vez")