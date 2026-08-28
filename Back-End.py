#começo de quando futuramente o aplicativo for feito
print("Olá, bom dia!")

saldo = 0

continuar = True

while continuar:

    print("1 - Adicionar saldo\n2 - Registrar despesas\n3 - ver saldo")

    N = int(input("Escolha um número: "))

    if N == 1:
        saldo_adicionado = float(input("Digite o saldo que deseja adicionar: "))
        print("Saldo adicionado.")
        saldo = saldo + saldo_adicionado

    elif N == 2:
        despesa = float(input("Digite o valor da despesa: "))
        if saldo >= despesa:
            saldo = saldo - despesa
            print("Despesa registrada com sucesso!")
        else:
            print("Saldo insuficiente para suprir despesa!")
    elif N == 3:
        print(saldo)

    else:
        print("opcao inválida")
    
    opcao = input("Deseja selecionar outro número? [S/N]")
    if opcao != 'S':
        continuar = False
