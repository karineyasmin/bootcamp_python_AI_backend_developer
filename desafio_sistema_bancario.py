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
cabecalho = '***'
menu = f'''
{cabecalho * 2} BANCO RIBEIRO {cabecalho * 2}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = [ ]


while True:
    
    opcao = input(menu).lower()
    
    if opcao == 'd':
        print(f'\nDepósito')
        deposito = float(input('\nQuanto você quer depositar? R$'))
        if deposito > 0:
            saldo += deposito
            extrato.append({'Depósito': deposito})
        else:
            print('\nValor de depósito não aceito.')
        print(f'\nSaldo atual: R${saldo:.2f}')
#----------------------------------------------------------------------------------------------------------------    
    elif opcao == 's':
        print('\nSaque') 
    
    
        if numero_saques < LIMITE_SAQUES:
            if saldo > 0:
                    print(f'\nSaldo: {saldo}')
                    saque = float(input('\nDigite o valor do saque: R$ '))
                    
                    if saque <= limite:
                        
                        if saque <= saldo:
                            
                            saldo -= saque
                            numero_saques += 1
                            print(f'\nSaldo: R${saldo:.2f}')
                            extrato.append({'Saque': saque})
                            
                        else:
                            print('\nSaldo insuficiente.')
                        
                    else:
                        print(f'\nValor acima do limite permitido de R${limite:.2f} por saque.')
                        
            else:
                print('\nNão há saldo disponível para saque.')
        else:
            print(f'\nQuantidade de saques diários excedidos.')

#---------------------------------------------------------------------------------------------------------------
    
    elif opcao == 'e':
        print('\nExtrato:')
        
        print(f'\n{extrato}')
        print(f'\nSaldo: R${saldo:.2f}')
    elif opcao == 'q':
        break
    
    else:
        print('\nOperação inválida, por favor selecione novamente a operação desejada.')    
        