'''
Desafio de Projeto - Criando um Sistema Bancário com Python_v.02

1. Objetivo: Incremento do sistema bancario, inserido limite de transações diárias, e registro de transações do sistema.

2. Histórico de Versões
   
    2.1. Versão 1: Criação do sistema
    2.2. Versão 2: Separar por funções, adicionar funcionalidades
    2.3. Versão 3: Adição de limites de uso diário para transações.

3. Funcionalidades adicionadas a cada versão
    
    3.1. Versão 1:
        Construção do sistema bancário básico: saldo, depósito, saque e extrato, conforme briefing.
        Incluida a Transferencia por Pix: limitado montante transferido diariamente: R$ 800,00; e valor unitario por pix: R$ 500,00.
    3.2. Versão 2:
        Otimização de código: separadas as funcionalidades existentes em funções.
        Incremento: criação das funções cadastramento de usuario e de conta bancária, e listagem de usuários e contas bancárias cadastradas.
    3.3. Versão 3:
        Incrementos: 
        a) adição de limite global de 10 transações diárias para saques, depositos e transferências por Pix. 
           O usuário deve ser informado quando o limite de transações diárias for excedido, e as transações não serão mais permitidas.
        b) Incluir data e hora das transações no extrato.
        c) Incluir registro histórico de todas as transações do sistema, com data e tipo de transação.   
'''

from datetime import datetime
from datetime import date

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
[9] Log do Sistema
[0] Sair
                         
Escolha a operação que gostaria de realizar: """)

def deposito(saldo, extrato): 
    deposito_valor = float(input("Informe o valor a depositar: "))
    if deposito_valor > 0:
        saldo += deposito_valor
        extrato.append({ 
            "data": datetime.today(),
            "tipo": "Depósito",
            "valor": deposito_valor})
        print(msg_confirmacao)
        historico_logs.append({
            "data": datetime.today(),
            "tipo": "Depósito"})    
    else:
        print(msg_acao_invalida)
    return saldo, extrato

def saque(saldo, extrato, saques_dia):
    if saques_dia >= LIMITE_SAQUES_DIARIO:
        print(msg_limite_transacoes)
    else:
        saque_valor = float(input("Informe o valor a sacar: "))
        if saque_valor > saldo:
            print(msg_sem_saldo)
        elif saque_valor > LIMITE_SAQUES_VALOR:
            print(msg_limite_valor)
        elif saque_valor > 0:
            saldo -= saque_valor
            extrato.append({ 
                "data": datetime.today(),
                "tipo": "Saque",
                "valor": saque_valor})
            saques_dia += 1
            print(msg_confirmacao)
            historico_logs.append({
            "data": datetime.today(),
            "tipo": "Saque"}) 
        else:
            print(msg_acao_invalida)
    return saldo, extrato, saques_dia

def pix (saldo, extrato, pix_vlr_dia):
    pix_valor = float(input("Informe o valor a transferir: ")) 
    if pix_valor > saldo:
        print(msg_sem_saldo)
    elif pix_valor > LIMITE_PIX_VALOR:
        print(msg_limite_valor)
    elif (pix_vlr_dia + pix_valor) > LIMITE_PIX_DIARIO:
        print(msg_limite_transacoes)
    elif pix_valor > 0:
        saldo -= pix_valor
        extrato.append({ 
            "data": datetime.today(),
            "tipo": "Pix Enviado",
            "valor": pix_valor})
        pix_vlr_dia += pix_valor
        print(msg_confirmacao)
        historico_logs.append({
            "data": datetime.today(),
            "tipo": "Pix Enviado"}) 
    else:
        print(msg_acao_invalida) 
    return  saldo, extrato, pix_vlr_dia

def exibir_extrato (saldo, extrato): 
    print("EXTRATO".center(60,'='))
    if not extrato:
        print('Não foram realizadas movimentações no período')      
    else:
        for transacao in extrato:
            data = transacao["data"]
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f'{data.strftime('%d/%m/%Y %H:%M')} - {tipo} no valor de: R$ {valor:.2f}')
        print(f'\nSaldo atual: R$ {saldo:.2f}')
        historico_logs.append({
            "data": datetime.today(),
            "tipo": "Extrato Exibido"}) 
    print("FIM".center(60,'=')) 

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
        historico_logs.append({
            "data": datetime.today(),
            "tipo": "Cadastro de Usuário"}) 

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
        historico_logs.append({
            "data": datetime.today(),
            "tipo": "Cadastro de Conta"}) 

def listar_usuarios():
    if not usuarios:
        print('Nenhum usuário cadastrado.\n')
        return
    else: 
        for indice, (cpf, nome, dt_nascimento, endereço) in enumerate(usuarios):
            print(f'{indice}: {cpf} - {nome} - {dt_nascimento} - {endereço}')
    historico_logs.append({
        "data": datetime.today(),
        "tipo": "Listagem de Usuários"}) 

def listar_contas():
    if not contas:
            print('Nenhuma conta cadastrada.\n')
            return    
    else:
        for indice, (numero_conta, agencia, cpf) in enumerate(contas):
            print(f'{indice}: Nr. Conta: {numero_conta}, Agência: {agencia}, CPF: {cpf}')
    historico_logs.append({
        "data": datetime.today(),
        "tipo": "Listagem de Contas"}) 

def qtdade_transacoes_dia(extrato):
    hoje = datetime.today().date()
    return sum(1 for transacao in extrato if transacao["data"].date() == hoje)

def log_sistema():
    print("Registro de Transações do Sistema".center(60,'='))
    if not historico_logs:
        print('Não foram realizadas movimentações no período')      
    else:
        for transacao in historico_logs:
            data = transacao["data"]
            tipo = transacao["tipo"]
            print(f'{data.strftime('%d/%m/%Y %H:%M')} - {tipo}')
    print("FIM".center(60,'=')) 


LIMITE_TRANSACOES_DIARIAS = 10
LIMITE_SAQUES_DIARIO = 3
LIMITE_SAQUES_VALOR = 500
LIMITE_PIX_DIARIO = 800
LIMITE_PIX_VALOR = 500

historico_logs = []                             # lista de transações do sistema
extrato = []                                    # deixa de ser string: vms usar como um dicionário
saques_dia = 0
pix_vlr_dia = 0
saldo = 0                                       # saldo da conta bancária

usuarios = []                                   # lista de tuplas: (cpf, nome, dt_nascimento, endereço)
contas = []                                     # lista de tuplas: (numero_conta, agencia, cpf)  
AGENCIA = '0001'

msg_sem_saldo = 'Não será possível realizar esta operação: saldo Insuficiente.\n'
msg_acao_invalida = 'Operação inválida. Por favor, informe um valor válido.\n'
msg_confirmacao = 'Operação realizada com sucesso!\n'
msg_limite_valor = 'Não será possível realizar esta operação: o valor excede o limite.\n'
msg_limite_transacoes = 'Não será possível realizar esta operação: a operação excede o limite de transações diárias.\n'

print("Bem-vindo ao Sistema Bancário Python!")
while True:
    opcao = menu() 
    if opcao in range(1, 3) and qtdade_transacoes_dia(extrato) > LIMITE_TRANSACOES_DIARIAS:
        print(msg_limite_transacoes)
        continue                                # interrompe o loop e volta para o menu
    elif opcao == '1': 
        print('Operação selecionada: Depósito.\n')
        saldo, extrato = deposito(saldo, extrato)
    elif opcao == '2':
        print ('Operação selecionada: Saque.\n')
        saldo, extrato, saques_dia = saque(saldo, extrato, saques_dia)
    elif opcao == '3':
        print ('Operação selecionada: Transferência por Pix.\n')
        saldo, extrato, pix_vlr_dia = pix(saldo, extrato, pix_vlr_dia)
    elif opcao == '4':
        print ('Operação selecionada: Extrato.\n')
        exibir_extrato(saldo, extrato)
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
    elif opcao == '9':
        print('Operação selecionada: Log do Sistema.\n')
        log_sistema()
    elif opcao == '0':
        print('Acesso Encerrado. Obrigada por ser nosso cliente!\n')
        break
    else:
        print(msg_acao_invalida) 
print()
