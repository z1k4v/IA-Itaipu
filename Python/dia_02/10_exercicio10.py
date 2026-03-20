# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

#%%
#Recebendo o input "Nome"
nome = input("Insira seu nome completo: ")
nome = nome.lower().split()
#Verificando se pertence a familia "calvo" e/ou "silva"
familiacalvo = "calvo"
familiasilva = "silva"
if familiacalvo in nome:
    print("Parabéns, você faz parte da família 'calvo'")
if familiasilva in nome:
    print("Parabéns, você faz parte da família 'silva'")
else:
    print("Lamento, você não faz parte da família.")