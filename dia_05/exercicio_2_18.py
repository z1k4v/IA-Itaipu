#Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases, ele pode apenas apertar o “enter”.
#Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

#%%
dados = {}
while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1
items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)
for i, j in items:
    print(i, " = ", j)