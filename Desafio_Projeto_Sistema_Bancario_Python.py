#Desafio de Projeto - Criando um Sistema Bancário com Python

#1. Objetivo: Criar sistema bancario

#2. Requisitos e Funcionalidades:

#   Versão 1: trabalha com apenas 1 usuário, não será necessário módulo de identificação do usuário.
#   Deve ser possível depositar valores positivos.
#   Todos os depósitos e saques devem ser armazenados em variáveis.
#   A movimentação deve ser exibida em um extrato.
#   Final do extrato deve exibir o saldo atual.
#   Valores dever ser exibidos no formato 'R$ xxx.xx'.
#   Permitir apenas 3 saques diários.
#   Limite máximo por saque é de R$ 500,00.
#   Mensagem ausencia de saldo: 'Não será possível sacar o dinheiro, por falta de saldo.'.

#3. Funcionalidades Adicionadas:

# Incluida a Transferencia por Pix.
# Limitado o montante a ser transferido diariamente a R$ 800,00
# Limitado o valor unitario de cada pix a R$ 500,00

#4. Código da Aplicação

LIMITE_SAQUES_DIA = 3
LIMITE_PIX_DIA = 800
limite_saque_valor = 500
limite_pix_valor = 500

extrato = '' #string]
saldo = 0
qtdade_saques_dia = 0
valor_sum_pix_dia = 0

msg_sem_saldo = 'Não será possível sacar o dinheiro, por falta de saldo.'
msg_acao_invalida = 'Operação inválida. Por favor, informe um valor válido.'
msg_confirmacao = 'Operação realizada com sucesso!\n'


menu = """
Escolha a operação que gostaria de realizar:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Pix
[0] Sair

"""

while True:
    opcao = input(menu)
    
#Operação 1 - Deposito
    if opcao == '1': 
        print('Operação selecionada: Depósito.')
        deposito_valor = float(input("Informe o valor a depositar: "))
        if deposito_valor > 0:
            saldo += deposito_valor
            extrato += f'Deposito no valor de: R$ {deposito_valor:.2f}\n'
            print(msg_confirmacao)
        else:
            print(msg_acao_invalida)
    
#Operação 2 - Saque
    elif opcao == '2':
        print ('Operação selecionada: Saque.')
        saque_valor = float(input("Informe o valor a sacar: "))
        if saque_valor > saldo:
            print('Não será possível realizar esta operação: saldo Insuficiente.')
        elif saque_valor > limite_saque_valor:
            print('Não será possível realizar esta operação: o valor excede o limite por saque.')
        elif qtdade_saques_dia > LIMITE_SAQUES_DIA:
            print('Não será possível realizar esta operação: a operação excede o limite de saques diários.')
        elif saque_valor > 0:
            saldo -= saque_valor
            extrato += f'Saque no valor de: R$ {saque_valor: .2f}\n'
            qtdade_saques_dia += 1
            print(msg_confirmacao)
        else:
            print(msg_acao_invalida)
    
#Operação 3 - Extrato   
    elif opcao == '3':
        print("EXTRATO".center(36,'='))
        if not extrato:
            print('Não foram realizadas movimentações no período')
            print("FIM".center(36,'='))
        else:
            print(extrato)
            print(f'\nSaldo atual: R$ {saldo:.2f}')
            print("FIM".center(36,'='))

#Operação 4 - Pix      
    elif opcao == '4':
        print ('Operação selecionada: Transferência por Pix.')
        pix_valor = float(input("Informe o valor a transferir: "))
        if pix_valor > saldo:
            print('Não será possível realizar esta operação: saldo Insuficiente.')
        elif pix_valor > limite_pix_valor:
            print('Não será possível realizar esta operação: o valor excede o limite de transferência.')
        elif (valor_sum_pix_dia + pix_valor) > LIMITE_PIX_DIA:
            print('Não será possível realizar esta operação: a operação excede o limite de transferências diários.')
        elif pix_valor > 0:
            saldo -= pix_valor
            extrato += f'Pix no valor de: R$ {pix_valor: .2f}\n'
            valor_sum_pix_dia += pix_valor
            print(msg_confirmacao)
        else:
            print(msg_acao_invalida) 
            
    elif opcao == '0':
        print('Acesso Encerrado. Obrigada por ser nosso cliente!')
        break
    else:
        print(msg_acao_invalida) 
        print()