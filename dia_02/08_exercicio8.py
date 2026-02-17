# Faça um programa de uma sorveteria onde o usuário pode escolher:
#   a. Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50) ou cestinha (R$4,00)
#   b. Sabor do sorvete: morango, creme ou chocolate
#   c) Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50) ou sem cobertura (R$0,00)
# Apresente o valor a ser pago
 
print("""Bem-vindo à sorveteria online!
      Por gentileza, informe qual tamanho de sorvete deseja.""")
# Escolha do tamanho
conta = 0
tamanho =   input("""Digite:
                    (1) casquinha - (R$1,00)
                    (2) cascão - (R$2,50)
                    (3) cestinha - (R$4,00)            
                    """)
if tamanho in ("1", "um", "Um"):
    conta = 1.00
elif tamanho in ("2", "dois", "Dois"):
    conta = 2.50
elif tamanho in ("3", "tres", "Tres"):
    conta = 4.00

if conta == 0:
    print("""Opção inválida.""")
# Escolha do sabor
else:
    sabor = input("""Escolha o sabor:
                    (1) morango
                    (2) creme
                    (3) chocolate
                    """)
    if sabor in ("1", "um", "Um"):
        sabor = "morango"

    elif sabor in ("2", "dois", "Dois"):
        sabor = "creme"

    elif sabor in ("3", "tres", "Tres"):
        sabor = "chocolate"
    
    else:
        sabor = 0

    if sabor == 0:
        print("""Opção inválida.""")
# Escolha da cobertura
    else:
        cobertura = input("""Escolha a cobertura:
                    (1) caramelo (R$1,50)
                    (2) morango (R$1,50)
                    (3) chocolate (R$1,50)
                    (4) sem cobertura (R$0,00)
                    """)
        if cobertura in ("1", "um", "Um"):
            cobertura= "caramelo"
            valor_cobertura = 1.50

        elif cobertura in ("2", "dois", "Dois"):
            cobertura = "morango"
            valor_cobertura = 1.50

        elif cobertura in ("3", "tres", "Tres"):
            cobertura = "chocolate"
            valor_cobertura = 1.50

        elif cobertura in ("4", "quatro", "Quatro"):
            cobertura = "sem cobertura"
            valor_cobertura = 0.00

        else:
            cobertura = 0

        if cobertura == 0:
                print("""Opção inválida.""")
    
        else:
            conta = conta + valor_cobertura
            print("O valor da sua conta é R$", conta,
                "Aqui está seu sorvete de", sabor, "com cobertura de", cobertura)