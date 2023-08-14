menu = input("Digite o serviço desejado \n 1 - deposito \n 2 - saque \n 3 - extrato \n 4 - sair")

saldo = 0
deposito = 0
saque = 0
limite = 500
numero_saques = 0
LIMITE_SAQUE = 3
hist_saque = []
hist_deposito = []

while True:

    opcao = input(menu)

    if opcao == "1":
        print("deposito")
        deposito = float(input("Qual valor voce deseja depositar? "))
        if deposito < 0:
            print("valor invalido")
        else:
            print(f"valor depositado R${deposito:.2f}")
        saldo = deposito + saldo
        print(f"seu saldo é R${saldo:.2f}")
        

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUE:
            print("Saque excedido")
        else:
            print("saque")
            saque = float(input("Qual valor voce deseja sacar?"))
            if saque>saldo:
                print("Saldo inferior ao saque")
            elif saque>500:
                print("Saque maior que R$500.00 nao permitido")
            else:
                saldo = saldo - saque
                print(f"Valor sacado R${saque:.2f}")
                print(f"Seu saldo agora é R${saldo:.2f}") 
        numero_saques = numero_saques + 1

    elif opcao == "3":
        print("extrato")
        print(f"Seu saldo é R${saldo:.2f}")
        if deposito!=0:
            print(f"Seu ultimo deposito foi de R${deposito:.2f}")
        else:
            pass
        if saque!=0:
            print(f"Seu ultimo saque foi de R${saque:.2f}")
        else:
            pass

    elif opcao == "4":
        break

    else:
        print("Operação invalida")







