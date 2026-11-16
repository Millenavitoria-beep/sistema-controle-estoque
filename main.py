
estoque = {}

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if nome in estoque:
        print("Esse produto já está cadastrado!")
        return

    quantidade = int(input("Quantidade inicial: "))
    preco = float(input("Preço do produto: R$ "))
    estoque[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }

    print("Produto cadastrado com sucesso!")


def consultar_estoque():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- ESTOQUE ATUAL ---")

    for nome, dados in estoque.items():
        print(f"Produto: {nome}")
        print(f"Quantidade: {dados['quantidade']}")
        print(f"Preço: R$ {dados['preco']:.2f}")

        if dados["quantidade"] <= 5:
            print("ALERTA: Estoque baixo!")

        print("--------------------")


def registrar_entrada():
    nome = input("Nome do produto: ").strip()

    if nome not in estoque:
        print("Produto não encontrado!")
        return

    quantidade = int(input("Quantidade de entrada: "))
    estoque[nome]["quantidade"] += quantidade

    print("Entrada registrada com sucesso!")


def registrar_saida():
    nome = input("Nome do produto: ").strip()

    if nome not in estoque:
        print("Produto não encontrado!")
        return

    quantidade = int(input("Quantidade de saída: "))

    if quantidade > estoque[nome]["quantidade"]:
        print("Quantidade insuficiente no estoque!")
        return

    estoque[nome]["quantidade"] -= quantidade
    print("Saída registrada com sucesso!")



def menu():
    while True:
        print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Consultar estoque")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_estoque()
        elif opcao == "3":
            registrar_entrada()
        elif opcao == "4":
            registrar_saida()
        elif opcao == "5":
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
