#Faça um programa que verifique se a pessoa pertence à família “calvo”.

#%%
#Recebendo o input "Nome"
nome = input("Insira seu nome completo: ")
nome = nome.lower().split()
#Verificando se pertence a familia "calvo"
familia = "calvo"
for i in nome:
    if i == familia:
        print("Parabéns, você faz parte da família 'calvo'")
if i != familia:
        print("Lamento, infelizmente você não faz parte da família 'calvo'")