#Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preçõs como valores. Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

#%%
frutas = {
    "Maçã":   "R$1.50", 
    "Banana": "R$2.75", 
    "Uva":    "R$1.90", 
    "Pera":   "R$1.25", 
    "Laranja":"R$0.65", 
    "Limão":  "R$1.25", 
    "Goiaba": "R$2.15", 
    "Abacaxi":"R$3.20", 
    "Jaca":   "R$5.80"
}

while True:
    fruta = input("Digite aqui a fruta desejada: ")
    if fruta == "":
        break
    if fruta in frutas:
        print(frutas[fruta])
    else:
        print("Entre com um item da lista: ")