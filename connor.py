#começo do código fazendo saudações para o usuário!
print("Olá, bom dia!")

#sistema cumprimentando conforme o seu nome.
nome = input("Qual é o seu nome? ")
print(f"Olá {nome}, seja bem-vindo(a) ao seu sistema de controle de saldo!")

#sistema de controle de saldo, onde o usuário pode adicionar saldo, registrar despesas e ver o saldo atual.

def menu():
    print("1 - Adicionar saldo\n2 - Registrar despesas\n3 - Ver saldo\n4 - Consultar histórico\n5 - Sair")

saldo = 0

while True:
    menu()
    N = int(input("Escolha um número: "))

    match N:
        case 1:
            valor = float(input("Digite o valor que deseja adicionar: "))
            historico1 = valor
            saldo += valor
            print(f"Saldo atual: R${saldo:.2f}")
        case 2:
            if saldo == 0:
                print("Atenção! Você não tem saldo suficiente para registrar despesas.")
            else:
                valor = float(input("Digite o valor da despesa: "))
                historico2 = valor
                if valor > saldo:
                    print("Atenção! Você não tem saldo suficiente para essa despesa.")
                else:
                    saldo -= valor
                    historico3 = valor
                print(f"Despesa registrada com sucesso!")
        case 3:
            print(f"Saldo atual: R${saldo:.2f}")
        case 4:
            print("Consultando histórico...")
            # Aqui você pode implementar a lógica para consultar o histórico de transações
            print("Histórico de transações:")
            # Exemplo de como exibir o histórico (substitua por sua implementação real)
            if 'historico1' in locals():
                print(f"- Adição de saldo: R${historico1:.2f}")
            if 'historico2' in locals():
                print(f"- Registro de despesa: R${historico2:.2f}")
            if 'historico3' in locals():
                print(f"- Despesa registrada: R${historico3:.2f}")
        case 5:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida, tente novamente.")