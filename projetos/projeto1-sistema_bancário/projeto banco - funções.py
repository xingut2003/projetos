def menu():
    menu = '''\n
============== MENU DE OPÇÕES ==============

[1] - Depósito

[2] - Saque

[3] - Extrato da conta

[4] - Cadastrar cliente

[5] - Novo usuário

[6] - Lista contas

[7] - Finalizar

'''
    return input(f'{menu}\nDigite sua opção: ')


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'\n\033[0;32mDepósito: R${valor}\033[m\n'
        print(f'\n\033[1;32mDepósito de R${valor} realizado com sucesso!\033[m\n')

    else:
        print('\n\033[1;31m**Falha de operação (valor digitado é inválido)**\033[m\n')

    return saldo, extrato

def saque(saldo, valor, extrato, limite, numero_de_saque):
    if valor > saldo:
        print('\033[0;31m**Saldo insuficiente.\033[m')

    elif valor > limite:
        print('\033[0;31m**O valor ultrapassa do limite por saque de R$500.00 .\033[m')

    elif valor > 0:
        saldo -= valor
        extrato += f'\033[0;31mSaque: R${valor}\033[m\n'
        print(f'\033[1;32mSaque de R${valor} realizado com sucesso!\033[m')
        numero_de_saque += 1

    else:
        print('\033[0;31mValor inválido!\033[m')
    return saldo, extrato, numero_de_saque


def mostrar_extrato(saldo, extrato):
    if not extrato:
        print('\033[1;31m**Não houve movimentação na sua conta bancária**\033[m')

    else:
        print(f'''
        ========== EXTRATO ==========
        {extrato}        
        Saldo = R${round(saldo, 2)}
        =============================
                ''')


def criar_usuario(usuarios):
    cpf = str(input('Digite seu CPF(somente números): '))
    usuario = filtro_de_usuarios(cpf, usuarios)

    if usuario:
        print('\n\033[0;31m*CPF já cadastrado!*\033[m')
        return

    nome = input('Digite seu nome completo: ').strip().upper()
    nascimento = str(input('Digite sua data de nascimento (dd-mm-aaaa): '))
    endereco = str(input('Informe seu endereço: ')).strip().title()

    usuarios.append({'Nome': nome, 'CPF': cpf, 'Nascimento': nascimento, 'Endereço': endereco})
    print(f'\n\033[0;32mSeu usuário foi criado com sucesso!\033[m')


def filtro_de_usuarios(cpf, usuarios):
    usuarios_filtrados = []

    for usuario in usuarios:

        if usuario['CPF'] == cpf:
            usuarios_filtrados.append(usuario)

    if usuarios_filtrados:
        return usuarios_filtrados[0]

    else:
        return None


def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = str(input('Digite seu CPF somente em números: '))
    usuario = filtro_de_usuarios(cpf, usuarios)

    if usuario:
        print('\033[0,32mParabéns! Sua conta foi criada!\033[m')
        return {'agência': agencia, 'número da conta': numero_da_conta, 'usuário': usuario}

    else:
        print('\033[0;31m*Usuário não encontrado*\033[m')
        return None


def lista_contas(contas):
    for conta in contas:
        print(f'''\\
        Agência: {conta['agência']}
        C/C: {conta['número da conta']}
        Titular: {conta['usuário']['Nome']}
        \n\n
        ''')


def comeco_programa():
    AGENCIA = '0001'
    limite_diario = 3
    saldo = 0.0
    limite_de_saque = 500
    extrato = ''
    numero_de_saque = 0
    usuarios = []
    contas = []

    while True:
        operacao = menu()
        if operacao == '1':
            valor = float(input('Digite o valor do seu depósito: '))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif operacao == '2':

            if numero_de_saque == limite_diario:
                print('\033[1;31m**Você atingiu o limite de saques diários**\033[m')

            else:
                valor = float(input('Digite o valor do seu saque: '))
                saldo, extrato, numero_de_saque = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite_de_saque,
                                       numero_de_saque=numero_de_saque)
            
        elif operacao == '3':
            mostrar_extrato(saldo, extrato)

        elif operacao == '4':
            criar_usuario(usuarios)

        elif operacao == '5':
            numero_da_conta = len(contas) + 1
            nova_conta = criar_conta(AGENCIA, numero_da_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)

        elif operacao == '6':
            lista_contas(contas)

        elif operacao == '7':
            break

        else:
            print('\033[1;31m**Operação inválida! Digite uma opção novamente**\033[m')


comeco_programa()

#Desenvolvedor: Davi Araújo Tymburibá Rêgo
