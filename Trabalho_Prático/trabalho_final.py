import os
import csv
def cadastrar_usuario(): # Essa função cria um novo perfil seja ele cliente, funcionario ou gerente. Armazenando as informações no arquivo csv de usuario.
    print("\nTela de Cadastro:")
    nome = input("Escolha um nome de usuário: ")
    senha = input("Crie uma senha: ")
    perfil = input("Digite o perfil (gerente, funcionario, cliente, etc): ")
    if not os.path.exists("usuarios.csv"):
        with open("usuarios.csv", mode="w", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["nome", "senha", "perfil"])
    with open("usuarios.csv", mode="a", newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, senha, perfil])

    print("Usuário cadastrado com sucesso!")
def fazer_login(): # Essa função faz com que a entrada de dados do usuario, seja tratada pelo sistema, vendo se os dados batem com o "banco de dados" (arquivo usarios.csv), se estiverem corretos dao acesso ao sistema, se não retorna dados incorretos.
    print("\nTela de Login:")
    nome = input("Nome de Usuário: ")
    senha = input("Senha: ")

    try:
        with open("usuarios.csv", mode="r") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha["nome"] == nome and linha["senha"] == senha:
                    print(f"\nLogin bem-sucedido! Bem-vindo, {nome} ({linha['perfil']})")
                    return linha["perfil"] 
            print("Usuário ou senha incorretos!")
            return None
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Cadastre-se primeiro.")
        return None
def menu_por_perfil(perfil): # Essa função cria a interface do menu, permitindo o usuario visualizar e interagir com as funcionalidades.
    while True:
        print(f"\n=== Menu do {perfil.capitalize()} ===")

        if perfil == "gerente":
            print("1. Cadastrar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            print("5. Logout")

        elif perfil == "funcionario":
            print("1. Listar Produtos")
            print("2. Atualizar Produto")
            print("3. Logout")

        elif perfil == "cliente":
            print("1. Listar Produtos")
            print("2. Logout")

        else:
            print("Perfil não reconhecido.")
            break

        opcao = input("Escolha uma opção: ")

        if perfil == "gerente":
            if opcao == "1":
                cadastrar_produto()
            elif opcao == "2":
                print("\n1. Ordenar por nome\n2. Ordenar por preço")
                tipo = input("Escolha: ")
                if tipo == "1":
                    listar_produtos("nome")
                elif tipo == "2":
                    listar_produtos("preco")
                else:
                    print("Opção inválida!")
            elif opcao == "3":
                atualizar_produto()
            elif opcao == "4":
                remover_produto()
            elif opcao == "5":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida!")

        elif perfil == "funcionario":
            if opcao == "1":
                listar_produtos("nome")
            elif opcao == "2":
                atualizar_produto()
            elif opcao == "3":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida!")

        elif perfil == "cliente":
            if opcao == "1":
                listar_produtos("nome")
            elif opcao == "2":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida!")
def cadastrar_produto(): # Essa função permite ao gerente cadrastar novos produtos, nomeando-os, fornecendo o codigo e o preço. Os produtos cadrastrados são armazenados em um arquivo csv produtos
    print("\n=== Cadastro de Produto ===")
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    preco = input("Preço do produto: ")
    quantidade = input("Quantidade em estoque: ")

    if not os.path.exists("produtos.csv"):
        with open("produtos.csv", mode="w", newline='') as arq:
            escritor = csv.writer(arq)
            escritor.writerow(["codigo", "nome", "preco", "quantidade"]) 

    with open("produtos.csv", mode="r") as arq:
        leitor = csv.DictReader(arq)
        for linha in leitor:
            if linha["codigo"] == codigo:
                print(" Já existe um produto com esse código!")
                return
    with open("produtos.csv", mode="a", newline='') as arq:
        escritor = csv.writer(arq)
        escritor.writerow([codigo, nome, preco, quantidade])
        print("Produto cadastrado com sucesso!")
def listar_produtos(ordem="nome"): # Essa função lista os produtos presente no sistema, retornando lisatados em ordem alfabetica ou de preço.
    print("\n=== Lista de Produtos ===")

    if not os.path.exists("produtos.csv"):
        print("❌ Nenhum produto cadastrado.")
        return

    with open("produtos.csv", mode="r") as arq:
        leitor = csv.DictReader(arq)
        produtos = list(leitor)

    if not produtos:
        print("⚠️ Lista vazia.")
        return
    if ordem == "nome":
        produtos.sort(key=lambda p: p["nome"].lower())
    elif ordem == "preco":
        produtos.sort(key=lambda p: float(p["preco"]))

    print(f"\nProdutos ordenados por: {ordem.capitalize()}")
    print("-" * 40)
    for p in produtos:
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${float(p['preco']):.2f} | Qtd: {p['quantidade']}")
    print("-" * 40)
def atualizar_produto(): # Essa função perimite alterar os preços, nomes dos produtos, alterando os no arquivo csv produtos. Essa funcionalidade é atribuida apenas aos funcionarios e gerente
    print("\n=== Atualizar Produto ===")

    if not os.path.exists("produtos.csv"):
        print("❌ Nenhum produto cadastrado.")
        return

    codigo = input("Digite o código do produto a ser atualizado: ")

    atualizado = False
    produtos = []

    with open("produtos.csv", mode="r") as arq:
        leitor = csv.DictReader(arq)
        for linha in leitor:
            if linha["codigo"] == codigo:
                print(f"Produto encontrado: {linha['nome']} (R${linha['preco']}, Qtd: {linha['quantidade']})")
                novo_nome = input("Novo nome (ou Enter para manter): ")
                novo_preco = input("Novo preço (ou Enter para manter): ")
                nova_qtd = input("Nova quantidade (ou Enter para manter): ")

                if novo_nome:
                    linha["nome"] = novo_nome
                if novo_preco:
                    linha["preco"] = novo_preco
                if nova_qtd:
                    linha["quantidade"] = nova_qtd

                atualizado = True
                print("✅ Produto atualizado com sucesso!")

            produtos.append(linha)

    if not atualizado:
        print("❌ Produto não encontrado.")
        return
    with open("produtos.csv", mode="w", newline='') as arq:
        campos = ["codigo", "nome", "preco", "quantidade"]
        escritor = csv.DictWriter(arq, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(produtos)
def remover_produto():  # Essa função permite remover produtos do sistema(ou seja do arquivo produtos.cvs), essa funcionalidade é atribuida somente ao gerente.
    print("\n=== Remover Produto ===")

    if not os.path.exists("produtos.csv"):
        print("❌ Nenhum produto cadastrado.")
        return

    codigo = input("Digite o código do produto a ser removido: ")

    removido = False
    produtos_restantes = []

    with open("produtos.csv", mode="r") as arq:
        leitor = csv.DictReader(arq)
        for linha in leitor:
            if linha["codigo"] == codigo:
                print(f"Produto removido: {linha['nome']} (R${linha['preco']}, Qtd: {linha['quantidade']})")
                removido = True
                continue 
            produtos_restantes.append(linha)

    if not removido:
        print("❌ Produto não encontrado.")
        return
    with open("produtos.csv", mode="w", newline='') as arq:
        campos = ["codigo", "nome", "preco", "quantidade"]
        escritor = csv.DictWriter(arq, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(produtos_restantes)

    print("✅ Produto removido com sucesso.")
while True: # Bloco principal, permite ao usario se cadrastra, fazer login ou sair do sistema.
    print("Menu Principal: \nEscolha uma das opçoes abaixo : \n 1.Login \n 2.Cadastro \n 3.Sair do Sistema")
    opcoesMenu = int (input("Digite o numero referente a opção desejada (1/2/3): "))
    if(opcoesMenu == 1):
        perfil = fazer_login()
        if perfil:
            menu_por_perfil(perfil)
    elif(opcoesMenu == 2):
        cadastrar_usuario()
    elif(opcoesMenu == 3):
        print(" Saindo do Sistema...\n✅Operação concluida com Sucesso!")
        break
    else:
        print("Opção Invalida!\n")