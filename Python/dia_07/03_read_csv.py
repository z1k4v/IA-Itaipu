#%%
arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)
#%%

dados = dict()

chaves = lines[0].strip("\n").split(";")
for i in chaves:
   dados[i] = []

#%%

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    for j in range(0,   len(valores)):
        dados[chaves[j]].append(valores[j])

dados