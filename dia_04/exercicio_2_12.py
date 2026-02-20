# Escreva um programa que exiba os números de 1 a 100. Caso o número seja divisível por 3, exiba “Fizz” no seu lugar, e para múltiplos de 5 exiba “Buzz”. Caso seja divisível por ambos, exiba “FizzBuzz”.

#%%
lista = []
cont = 1
end = 100
div3 = "Fizz"
div5 = "Buzz"
div3e5 = "FizzBuzz"

for i in range(cont, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        lista.append(div3e5)
        i += 1
    elif i % 3 == 0:
        lista.append(div3)
        i += 1
    elif i % 5 == 0:
        lista.append(div5)
        i += 1
    else:
        lista.append(i)
        i += 1
print(lista)