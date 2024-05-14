# v1.0 - 08/04/24
# Autora: Karine Yasmin
#Regras no arquivo regras_v1.txt
# ---------------------------------------------------------------------------
menu = '''=-=-= Menu da Conta =-=-=

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
        print(f'Saldo atual: R${saldo:.2f}\n')
    elif opcao == 's':
        valor = float(input('\nInforme o valor do saque: R$ '))
        
        excede_saldo = valor > saldo
        
        excede_limite = valor > limite 
        
        excede_saques = numero_saques >= LIMITE_SAQUES 
        
        if excede_saldo:
            print('Saldo insuficiente.')
            
        elif excede_limite:
            print('\nOperação falhou! O valor excedeu o limite de saque.\n')
            
        elif excede_saques:
            print('\nQuantidade de saques diários excedidos.\n')
            
        elif valor > 0:
            saldo -= valor
            extrato += f'\nSaque de R$ {valor}'
            numero_saques += 1
             
        else:
            print('\nA operação falhou! O valor é inválido\n')
        print(f'\nSaldo atual: R${saldo:.2f}\n')
        

    elif opcao == 'e':
        
        print(f'=-=-= Extrato =-=-=')
        if not extrato:
            print('\nNão foram feitas operações.\n')
        else:        
        
            print(f'{extrato}\n')
        print(f'Saldo atual: R${saldo:.2f}')
        
        
        
    elif opcao == 'q':
        break
    
    else:
        print('\nOperação inválida, por favor selecione novamente a operação desejada.')    
        