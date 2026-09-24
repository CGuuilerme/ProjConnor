#começo do código fazendo saudações para o usuário!
print("Olá, bom dia!")

#sistema cumprimentando conforme o seu nome.
nome = input("Qual é o seu nome? ")
print(f"Olá {nome}, seja bem-vindo(a) ao seu sistema de controle de saldo!")

#sistema de controle de saldo, onde o usuário pode adicionar saldo, registrar despesas e ver o saldo atual.

def menu():
    print("1 - Adicionar saldo\n2 - Registrar despesas\n3 - Ver saldo")

saldo = 0

while True:
    menu()
    N = int(input("Escolha um número: "))

    if N == 1:
        valor = float(input("Digite o valor que deseja adicionar: "))
        saldo += valor
        print(f"Saldo atual: R${saldo:.2f}")
    elif N == 2:
        if saldo == 0:
            print("Atenção! Você não tem saldo suficiente para registrar despesas.")
            continue

        valor = float(input("Digite o valor da despesa: "))
        if valor > saldo:
            print("Atenção! Você não tem saldo suficiente para essa despesa.")
        else:
            saldo -= valor
            print(f"Saldo atual: R${saldo:.2f}")
    elif N == 3:
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("Opção inválida, tente novamente.")
