#v2.0 - 10/04/2024
#Autora: Karine Yasmin
#Regras no arquivo regras_v2.txt
#------------------------------------------------------------------------
def menu():
   exibir_menu = int(input('''
    =-=-= Menu da Conta =-=-=

    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Novo Usuário
    5 - Listar Contas
    6 - Nova Conta
    0 - Sair 
    >> '''))
   
   return exibir_menu
    
def despositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor 
            extrato += f'\nDepósito:\tR${valor:.2f}'
            print('\n=-=-= Depósito concluído com sucesso! =-=-=')   
                  
    else: 
        print('### Operação Falhou! O valor é inválido. ###')
           
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n### Operação falhou! Você não tem saldo suficiente. ###")

    elif excedeu_limite:
        print("\n### Operação falhou! O valor do saque excede o limite. ###")

    elif excedeu_saques:
        print("\n### Operação falhou! Número máximo de saques excedido. ###")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f'\n=-=-=-=-= Extrato =-=-=-=-=')
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo:\t\tR${saldo:.2f}')  
    print('=-=-=-=-==-=-=-=-=-=-=-=-=-=-=')
    return saldo, extrato

          
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n### Já existe um usuário com esse CPF! ###')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço(logradouro, número - bairro - cidade/UF): ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
    print('=-=-= Usuário criado com sucesso! =-=-=')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n=-=-= Conta criada com sucesso! =-=-=')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n### Usuário não encontrado, fluxo de criação de conta encerrado! ###')
    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)        


def main():
    '''Função principal'''  
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    numero_saques = 0    
    extrato = ''
    usuarios = []
    contas = []
    
    while True:
        
        opcao = menu()
        
        # Depositar:
        if opcao == 1:        
            valor = float(input('\nInforme o valor do depósito:\nR$')) 
            saldo, extrato = despositar(saldo, valor, extrato)
        
        # Saque:          
        elif opcao == 2:   
            
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
           
        # Extrato   
        elif opcao == 3:
            saldo, extrato = exibir_extrato(saldo, extrato=extrato)
        
        
        # Criar usuário
        elif opcao == 4:
                criar_usuario(usuarios)
                
        # Listar contas        
        elif opcao == 5 :
            listar_contas(contas)
        
        # Nova Conta 
        elif opcao == 6:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        # Sair    
        elif opcao == 0:
            print('\nEncerrando...')
            break    
            
        else:
            print('\nOpção inválida!\nTente novamente.\n')
        
main()