#%%
nome_arquivo = "teste_dos_testes.txt"

inserir = input("Digite aqui um texto a inserir: ")

# with open (nome_arquivo, mode="w") as open_file:
with open (nome_arquivo, mode="a") as open_file:
    open_file.write(inserir)