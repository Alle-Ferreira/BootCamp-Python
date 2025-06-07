# BootCamp-Python

Arquivos do Bootcamp de Desenvolvimento com Python

02/04/2025 - Desafio de Projeto 1: Sistema Bancário_v.01
- Construção do sistema bancário básico: saldo, depósito, saque e extrato, conforme briefing.
- Incluida a Transferencia por Pix: limitado montante transferido diariamente: R$ 800,00; e valor unitario por pix: R$ 500,00.

07/06/2025 - Desafio de Projeto 2: Sistema Bancário_v.02
- Otimização de código: separadas as funcionalidades existentes em funções.
- Incrementos: 
        a) criação das funções cadastramento de usuario: 
            - atributos: nome, data nascimento, cpf, e endereço (logradouro, número, complemento, bairro, cidade, estado e cep.)
            - regras de negócio: somente pode ser cadastrado um usuário por CPF.
        b) criação de conta bancária, vinculada ao cliente: 
            - atributos: número da conta, agência, usuário.
            - regras de negócio: numero da conta é sequencial, iniciando em 1; agência é fixo: 0001. 
            
07/06/2025 - Desafio de Projeto 3: Sistema Bancário_v.03
- Incrementos: 
        a) adição de limite global de 10 transações diárias para saques, depositos e transferências por Pix. 
           O usuário deve ser informado quando o limite de transações diárias for excedido, e as transações não serão mais permitidas.
        b) Incluir data e hora das transações no extrato.
        c) Incluir registro histórico de todas as transações do sistema, com data e tipo de transação. 
