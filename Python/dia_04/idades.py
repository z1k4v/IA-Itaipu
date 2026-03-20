#

#%%
idades = []
while True:
    idade = input("Insira aqui a idade: ")
    if idade == "":
        break
    idades.append(int(idade))
print(idades)