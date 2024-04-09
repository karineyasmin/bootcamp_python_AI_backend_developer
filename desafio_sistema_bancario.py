'''
Regras

Operação de depósito:

Deve ser possivel depositar valores positivos para a minha conta bancaria. A v1 do projeto trabalha apenas com 1 usuario，
dessa forma nao precisamos nos preocupar em identificar qual é o numero da agência e conta bancária. 
Todos os depositos devem ser armazenados em uma variável e exibidos na operação de extrato.
 
Operação de saque:
 
O sistema deve permitir realizar 3 saques diarios com limite maximo de R$ 500,00 por saque.
Caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que nao sera possivel sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. 
No fim da listagem deve ser exibido saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
exemplo:

1500.45=R$1500.45
'''
cabecalho = '=-=-=-=-=-=-'
menu = f'''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ''


while True:

    opcao = input(menu).lower()
    
    if opcao == 'd':
        valor = float(input('\nInforme o valor do depósito: R$ '))
        
        if valor > 0:
            saldo += valor
            extrato += f'\nDepósito de R${valor:.2f}'
            
            
        else:
            print('\nA operação falhou! O valor é inválido.')
        print(f'Saldo atual: R${saldo:.2f}\n{cabecalho * 3}')
#----------------------------------------------------------------------------------------------------------------    
    elif opcao == 's':
        valor = float(input('\nInforme o valor do saque: R$ '))
        
        excede_saldo = valor > saldo
        
        excede_limite = valor > limite 
        
        excede_saques = numero_saques >= LIMITE_SAQUES 
        
        if excede_saldo:
            print('Saldo insuficiente.')
            
        elif excede_limite:
            print('Operação falhou! O valor excedeu o limite de saque.')
            
        elif excede_saques:
            print('Quantidade de saques diários excedidos.')
            
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de R$ {saldo}'
            numero_saques += 1
             
        else:
            print('A operação falhou! O valor é inválido')
        print(f'Saldo atual: R${saldo:.2f}\n{cabecalho * 3}')
        
#---------------------------------------------------------------------------------------------------------------
    elif opcao == 'e':
        
        print(f'{cabecalho} Extrato {cabecalho}')
        if not extrato:
            print('Não foram feitas operações.')
        else:        
        
            print(f'{extrato}\n')
        print(f'\nSaldo atual: R${saldo:.2f}')
        print(cabecalho * 3)
        
        
    elif opcao == 'q':
        break
    
    else:
        print('\nOperação inválida, por favor selecione novamente a operação desejada.')    
        