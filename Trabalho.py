# Lista de clientes, funcionários e vendas
clientes = []
funcionarios = []
vendas = []

# Função para cadastrar cliente
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    telefone = input("Telefone do cliente: ")
    
    cliente = {"nome": nome, "cpf": cpf, "telefone": telefone}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

# Função para cadastrar funcionário
def cadastrar_funcionario():
    nome = input("Nome do funcionário: ")
    cpf = input("CPF do funcionário: ")
    cargo = input("Cargo do funcionário: ")
    
    funcionario = {"nome": nome, "cpf": cpf, "cargo": cargo}
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

# Função para registrar venda
def registrar_venda():
    cliente_id = int(input("ID do cliente: "))
    funcionario_id = int(input("ID do funcionário: "))
    litros = float(input("Quantidade de litros vendidos: "))
    valor_total = float(input("Valor total da venda: "))
    data = input("Data da venda (AAAA-MM-DD): ")
    
    venda = {"cliente_id": cliente_id, "funcionario_id": funcionario_id, "litros": litros, "valor_total": valor_total, "data": data}
    vendas.append(venda)
    print("Venda registrada com sucesso!")

# Função para gerar relatório de vendas
def gerar_relatorio_vendas():
    print("ID | Cliente ID | Funcionário ID | Litros | Valor Total | Data")
    for i, venda in enumerate(vendas, 1):
        print(f"{i} | {venda['cliente_id']} | {venda['funcionario_id']} | {venda['litros']} | {venda['valor_total']} | {venda['data']}")

# Menu principal
while True:
    print("1. Cadastrar cliente")
    print("2. Cadastrar funcionário")
    print("3. Registrar venda")
    print("4. Gerar relatório de vendas")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        cadastrar_funcionario()
    elif opcao == "3":
        registrar_venda()
    elif opcao == "4":
        gerar_relatorio_vendas()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
