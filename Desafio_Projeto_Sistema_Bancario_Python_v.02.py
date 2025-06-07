'''
Desafio de Projeto - Criando um Sistema Bancário com Python_v.02

1. Objetivo: Incremento do sistema bancario_Inserir limite uso diário

2. Histórico de Versões
   
    2.1. Versão 1: Criação do sistema
    2.2. Versão 2: Separar por funções, adicionar funcionalidades

3. Funcionalidades adicionadas a cada versão
    
    3.1. Versão 1:
        Construção do sistema bancário básico: saldo, depósito, saque e extrato, conforme briefing.
        Incluida a Transferencia por Pix: limitado montante transferido diariamente: R$ 800,00; e valor unitario por pix: R$ 500,00.
    3.2. Versão 2:
        Otimização de código: separadas as funcionalidades existentes em funções.
        Incremento: 
        a) criação das funções cadastramento de usuario: 
            - atributos: nome, data nascimento, cpf, e endereço (logradouro, número, complemento, bairro, cidade, estado e cep.)
            - regras de negócio: somente pode ser cadastrado um usuário por CPF.
        b) criação de conta bancária, vinculada ao cliente: 
            - atributos: número da conta, agência, usuário.
            - regras de negócio: numero da conta é sequencial, iniciando em 1; agência é fixo: 0001.
        c) criação de lista de usuários e contas bancárias cadastradas.     
'''

def menu():
    return input("""Menu:
                 
[1] Depositar
[2] Sacar
[3] Pix
[4] Extrato
[5] Cadastrar Usuário
[6] Cadastrar Conta
[7] Listar Usuários
[8] Listar Contas
[0] Sair
                         
Escolha a operação que gostaria de realizar: """)
    print()

def deposito(saldo, extrato, /): # passagem por posição: '/' no final
    deposito_valor = float(input("Informe o valor a depositar: "))
    if deposito_valor > 0:
        saldo += deposito_valor
        extrato += f'Deposito no valor de: R$ {deposito_valor:.2f}\n'
        print(msg_confirmacao)
    else:
        print(msg_acao_invalida)
    return saldo, extrato
    print()

def saque(*, saldo, extrato, saques_dia):   # passagem por nome: '*' no inicio
    saque_valor = float(input("Informe o valor a sacar: "))
    if saque_valor > saldo:
        print('Não será possível realizar esta operação: saldo Insuficiente.')
    elif saque_valor > LIMITE_SAQUES_VALOR:
        print('Não será possível realizar esta operação: o valor excede o limite por saque.')
    elif saques_dia > LIMITE_SAQUES_DIARIO:
        print('Não será possível realizar esta operação: a operação excede o limite de saques diários.')
    elif saque_valor > 0:
        saldo -= saque_valor
        extrato += f'Saque no valor de: R$ {saque_valor: .2f}\n'
        saques_dia += 1
        print(msg_confirmacao)
    else:
         print(msg_acao_invalida)
    return saldo, extrato, saques_dia
    print()

def pix (saldo, extrato, pix_vlr_dia, LIMITE_PIX_DIARIO, LIMITE_PIX_VALOR):
    pix_valor = float(input("Informe o valor a transferir: ")) 
    if pix_valor > saldo:
        print(msg_sem_saldo)
    elif pix_valor > LIMITE_PIX_VALOR:
        print(msg_limite_transacao)
    elif (pix_vlr_dia + pix_valor) > LIMITE_PIX_DIARIO:
        print(msg_limite_transacao)
    elif pix_valor > 0:
        saldo -= pix_valor
        extrato += f'Pix no valor de: R$ {pix_valor: .2f}\n'
        pix_vlr_dia += pix_valor
        print(msg_confirmacao)
    else:
        print(msg_acao_invalida) 
    return  saldo, extrato, pix_vlr_dia

def exibir_extrato (saldo, /, *, extrato): # saldo posicional '/', extrato nomeado '*'
    print("EXTRATO".center(40,'='))
    if not extrato:
        print('Não foram realizadas movimentações no período')      
    else:
        print(extrato)
        print(f'\nSaldo atual: R$ {saldo:.2f}')
    print("FIM".center(40,'=')) 
    return
    print()

def cad_usuario():
    cpf = input('Informe o CPF do novo usuário (somente números): ')
    if cpf in [usuario[0] for usuario in usuarios]:
        print(f'Usuário já cadastrado com este CPF: usuário {usuarios.index(cpf)}')
        return
    elif len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido. Deve conter 11 dígitos numéricos.')
        return
    else:
        nome = input('Informe o nome completo do usuário: ')
        dt_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
        endereco = input('Informe logradouro, numero, complemento, bairro, cidade, uf, cep, separados por vírgula:\n')
        usuarios.append((cpf, nome, dt_nascimento, endereco))
    print(f' Usuário cadastrado com sucesso! \nCPF: {cpf} \nData de Nascimento: {dt_nascimento} \nNome: {nome} \nEndereço: {endereco}')
    print()

def cad_conta():
    cpf = input('Informe o CPF do usuário (somente números): ')
    if len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido. Deve conter 11 dígitos numéricos.')
        return 
    elif cpf not in [usuario[0] for usuario in usuarios]:
        print('Nenhum usuário cadastrado. Necessário cadastrar um usuário primeiro.')
        return
    else:
        numero_conta = len(contas) + 1
        contas.append((numero_conta, AGENCIA, cpf))
        print(f'Conta bancária cadastrada com sucesso: \nNr. Conta: {numero_conta} - Agência: {AGENCIA} \nCPF Usuário: {cpf}')
    print()

def listar_usuarios():
    if not usuarios:
        print('Nenhum usuário cadastrado.\n')
        return
    else: 
        for indice, (cpf, nome, dt_nascimento, endereço) in enumerate(usuarios):
            print(f'{indice}: {cpf} - {nome} - {dt_nascimento} - {endereço}')
    print()

def listar_contas():
    if not contas:
            print('Nenhuma conta cadastrada.\n')
            return    
    else:
        for indice, (numero_conta, agencia, cpf) in enumerate(contas):
            print(f'{indice}: Nr. Conta: {numero_conta}, Agência: {agencia}, CPF: {cpf}')
    print()


print("Bem-vindo ao Sistema Bancário Python!")

LIMITE_SAQUES_DIARIO = 3
LIMITE_SAQUES_VALOR = 500
LIMITE_PIX_DIARIO = 800
LIMITE_PIX_VALOR = 500

extrato = ''                                    #string
saldo = 0
saques_dia = 0
pix_vlr_dia = 0

usuarios = []                                   # lista de tuplas: (cpf, nome, dt_nascimento, endereço)
contas = []                                     # lista de tuplas: (numero_conta, agencia, cpf)  
AGENCIA = '0001'

msg_sem_saldo = 'Não será possível realizar esta operação: saldo Insuficiente.\n'
msg_acao_invalida = 'Operação inválida. Por favor, informe um valor válido.\n'
msg_confirmacao = 'Operação realizada com sucesso!\n'
msg_limite_transacao = 'Não será possível realizar esta operação: o valor excede o limite.\n'

while True:
    opcao = menu() 
    
    if opcao == '1': 
        print('Operação selecionada: Depósito.\n')
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == '2':
        print ('Operação selecionada: Saque.\n')
        saldo, extrato, saques_dia = saque(
            saldo = saldo, 
            extrato = extrato, 
            saques_dia = saques_dia)

    elif opcao == '3':
        print ('Operação selecionada: Transferência por Pix.\n')
        saldo, extrato, pix_vlr_dia = pix (saldo, extrato, pix_vlr_dia, LIMITE_PIX_DIARIO, LIMITE_PIX_VALOR)

    elif opcao == '4':
        print ('Operação selecionada: Extrato.\n')
        exibir_extrato(saldo, 
            extrato = extrato)

    elif opcao == '5':   
        print('Operação selecionada: Cadastrar Usuário.\n')
        cad_usuario()

    elif opcao == '6':
        print('Operação selecionada: Cadastrar Conta.\n')
        cad_conta() 

    elif opcao == '7':
        print('Operação selecionada: Listar Usuários.\n')
        listar_usuarios()

    elif opcao == '8':
        print('Operação selecionada: Listar Contas.\n')
        listar_contas()
        
    elif opcao == '0':
        print('Acesso Encerrado. Obrigada por ser nosso cliente!\n')
        break
    else:
        print(msg_acao_invalida) 
print()