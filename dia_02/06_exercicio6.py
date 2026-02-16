# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

print("Bem-vindo à venda online de água! Por gentileza, informe se deseja água mineral natural ou água mineral com gás.")

conta = 0
tipo_agua = input("""Digite:
(1) água mineral natural
(2) água mineralcom gás              
""")
if tipo_agua == "1":
    conta = 1.50
elif tipo_agua == "2":
    conta = 2.50
    print("Você escolheu água mineral com gás. O valor a ser pago é R$2,50.")

if conta == 0:
    print("Opção inválida.")
else:
    print("O valor da sua conta é R$", conta)