#Lista para armazenar os dados em memória
clientes = []

#Menu pricipal com laço de repetição
opcao = ""

while opcao != "4":
    print("\n=== Sistema de Cadastro de Clientes ===")
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Buscar Cliente")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Cadastro de cliente             
        nome = input("Digite o nome do cliente:")
        idade = input("Digite a idade do cliente:")
        email = input("Digite o email do cliente:")
        telefone = input("Digite o telefone do cliente:")
        clientes.append({"nome": nome,"idade": idade,"email": email,"telefone": telefone})

        print(f"Cliemte: '{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== Lista de Clientes Cadastrados ===")
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                print(f"Nome: {c['nome']}, "
                     f"Idade: {c['idade']}, "
                     f"Email: {c['email']}, "
                     f"Telefone: {c['telefone']}")

    elif opcao == "3":
            busca = input("Digite o nome do cliente para buscar:").lower()
            encontrado = False

            for c in clientes:
                if busca in c["nome"].lower():
                    print(
                        f"Nome: {c['nome']}, "
                        f"Idade: {c['idade']}, "
                        f"Email: {c['email']}, "
                        f"Telefone: {c['telefone']}"
                    )
                    encontrado = True

            if not encontrado:
                print("Cliente não encontrado.")

    elif opcao == "4":
        print("Encerrando sistema...")
