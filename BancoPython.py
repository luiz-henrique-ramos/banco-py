menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

"""

saldo = 0
limite = 5000
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3 

while True:
    
    opcao = input(menu).lower()
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito = R$ {valor:.2f}\n"
            continue
        else:
            print("Operação falhou! O valor informado é inválido.")    
            continue
            
    if opcao == "s":
        valor = float(input("Defina o valor do Saque: "))
        
        excedeu_limite_saques = numero_saques > LIMITE_SAQUES
        excedeu_limite = valor > limite
        
        if excedeu_limite_saques:
            print("Operação falhou! Você excedeu o numero de saques diários.")
            continue
        
        if excedeu_limite:
            print(f"Operação falhou! O valor ultrapassou o limite de R$ {limite:.2f}.")
            continue
        
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"Saque = R$ {valor:.2f}\n"
            numero_saques += 1
            continue
        
        if valor > saldo:
            print("Operação falhou! O valor é maior que o seu saldo.")
            continue
        else:
            print("Operação falhou! O valor informado é inválido.")
            continue
    
    if opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        continue
    
    if opcao == "q":
        break

    print("Operação inválida, por favor selecione novamente a operação desejada.")        