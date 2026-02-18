#Escreva um código que receba uma entrada em texto (String) e diga se a String é ou não um Palíndromo
#%%
#definindo variáveis
texto = input("Insira o texto: ")
texto = texto.replace(" ", "").lower()
inverso = ""
#invertendo a palavra
for i in range(len(texto) -1, -1, -1):
    inverso += texto[i]
#verificando palíndromos
if inverso == texto:
    print("Temos um palíndromo", texto, "=", inverso)
else:
    print("Essa frase", texto, "não é um palíndromo")