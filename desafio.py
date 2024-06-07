def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar usuário
    [nc] Criar conta
    [q] Sair

    => """
    return input(menu)


def realizar_saque(*, valor, saldo, extrato, saques_n, limite, limite_saques):

    saldo_negativo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = saques_n > limite_saques

    if saldo_negativo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saque:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        saques_n += 1
        print(f"Valor do saque realizado: R$ {valor:.2f}")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def depositar(
    saldo,
    valor,
    extrato,
):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ Extrato ================")
    if not extrato:
        print("Não houve movimentações realizadas!")
    else:
        extrato
        print(f"\nSaldo: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário cadastrado com esse CPF!")
        return

    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }
    )

    print("Usuário cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    found_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return found_usuario[0] if found_usuario else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuarios}

    print("Usuário não encontrado!")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    saques_n = 0
    limite_saques = 3
    usuarios = []
    contas = []
    numero_conta = 1
    agencia = "0001"

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor para saque: "))

            saldo, extrato = realizar_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques_n=saques_n,
                limite_saques=limite_saques,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
