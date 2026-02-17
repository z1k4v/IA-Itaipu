# Escreva um código que imprima a tabuada de 1 a 10, de forma organizada e clara.
#%%
# Definindo as variáveis 
count = 1
multp = 1

# Realizando a tabuada
while count <= 10:
    while multp <=10:
        print(count, "X", multp, "=", count * multp)
        multp = multp + 1
    print("")
    multp = 1
    count = count + 1