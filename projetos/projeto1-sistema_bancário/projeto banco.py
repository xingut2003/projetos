# Módulo de um sistema bancário em linguagem Python 3.

# Um texto base para iniciar o atendimento no sistema de banco.

print('Seja bem vindo ao banco (Nome_Do_Banco)! Iremos te encaminhar para o menu de opções.\n\n')

# Criando uma string de várias linhas e armazenar em uma variável.

menu = '''
============== MENU DE OPÇÕES ==============

[1] - Depósito

[2] - Saque

[3] - Extrato da conta

[4] - Finalizar

'''

# Colocando cada variável com os dados desejados.

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

# Inserindo um sistema de loop tipo "while()" para que o usuário tenha a total autonomia de
# finalizar suas operações assim que desejar. Além disso, o indivíduo tem o direito de
# realizar uma das quatro opções de operações, simplismente digitando o número desejado.

while(True):

    opcao = input(f'{menu}Digite sua opção: ')

# Nesta opção, o usuário pode digitar o valor do depósito que quiser e se digitar algum valor
# menor que zero, o sistema irá retornar inválido e permitindo-o a digitar infinitas vezes até
# ter um valor válido maior que zero.

    if(opcao == '1'):

        while(True):
            valor = float(input('\nDigite o valor do depósito: '))

            if(valor>0):
                extrato += f'\nDepósito: R${round(valor)}\n'
                saldo += valor
                print(f'\nDepósito de R${round(valor, 2)} realizado com sucesso!\n')
                break

            else:
                print('\nFalha de operação (valor digitado é inválido)\n')

# Aqui a pessoa que estará fazendo o saque, tem um limite por saque de R$500,00 por vez como a variável
# acima está explicita e não permitindo valores negativos; como também, não pode sacar mais que três vezes
# por dia e caso tente, será direcionada ao menu novamente

    elif(opcao == '2'):
        if (numero_de_saques == LIMITE_DE_SAQUES):
            print('Não foi possível realizar esta operação. Limite de saque diário atingido.')

        else:
            while(True):
                valor_saque = float(input('\nDigite o valor de saque: '))

                if(valor_saque <= limite and valor_saque > 0 and valor_saque <= saldo):
                    numero_de_saques += 1
                    extrato += f'\nSaque: R${valor_saque}\n'
                    saldo -= valor_saque

                    print(f'\nSaque de R${round(valor_saque, 2)} realizado com sucesso!\n')
                    break
                elif(valor_saque > limite):
                    print('\nSaque não efetuado. Valor maior que o limite por saque R$ 500.00 .\n')

                elif(valor_saque < 0):
                    print('\nSaque não efetuado. Valor inválido.\n')

# Na opção "3" ela irá ver o extrato e podendo observar quantos depósitos e saques ocorream em ordem
# de ação, também o saldo final da conta com os depósitos e saque feitos.

    elif(opcao == '3'):
        print(f'''
========== EXTRATO ==========
{extrato}        
Saldo = R${round(saldo, 2)}
=============================
        ''')

# A última opção ela irá sair do sistema e finalizando as operações.

    elif(opcao == '4'):
        print('Obrigado por usar o banco XXX!')
        break

# Este "else" é caso o usuário digite algo diferente de "1,2,3 ou 4" nas opções de operações.

    else:
        print('Operação inválida.')

#Desenvolvedor: Davi Araújo Tymburibá Rêgo