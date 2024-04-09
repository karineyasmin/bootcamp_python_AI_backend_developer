# v1.0 - 08/04/24
# Autora: Karine Yasmin
# ---------------------------------------------------------------------------
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
        