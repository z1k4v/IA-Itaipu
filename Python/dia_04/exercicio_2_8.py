# Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

#%%
media = 0
menor = 0
maior = 0
uniao = []
qtd_notas = 4

for i in range(qtd_notas):
    nota = int(input("Insira aqui a sua nota: "))
    uniao.append(nota)

media = sum(uniao) / len(uniao)
minimo = min(uniao)
maximo = max(uniao)

print(media)
print(minimo)
print(maximo)