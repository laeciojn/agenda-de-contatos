contato = {"nome": "",
           "telefone": "",
           "email": "",
           "favorito": False}

contatos = []

def adicionar_contato(contato):
    contato["nome"] = input("Digite o nome do contato: ")
    contato["telefone"] = input("Digite o telefone do contato: ")
    contato["email"] = input("Digite o e-mail do contato: ")
    contatos.append(contato.copy())
    print(f"Contato do(a) {contato['nome']} salvo com sucesso!")

def visualizar_contatos():
    print("\nLista de contatos")
    for indice, c in enumerate(contatos, start=1):
        print(f"\nContato {indice}")
        print(f"Nome: {c['nome']}")
        print(f"Telefone: {c['telefone']}")
        print(f"E-mail: {c['email']}")
        print(f"Favorito: {c['favorito']}")

def editar_contato_existente():
    visualizar_contatos()
    numero = int(input("Informe o número do contato que deseja atualizar: "))

    if numero < 1 or numero > len(contatos):
        print("Número não encontrado")
        return

    contato = contatos[numero - 1]
    contato["nome"] = input("Digite o novo nome: ")
    contato["telefone"] = input("Digite o novo telefone: ")
    contato["email"] = input("Digite o novo e-mail: ")
    print("Contato editado com sucesso.")



def marcar_desmarcar_contato_favorito():
    visualizar_contatos()
    num = int(input("Informe o número do contato: "))
    if num < 1 or num > len(contatos):
        print("Número não encontrado")
        return

    contato = contatos[num - 1]
    contato["favorito"] = not contato["favorito"]

    if contato["favorito"]:
        print(f"Contato {contato['nome']} marcado como favorito.")
    else:
        print(f"Contato {contato['nome']} removido dos favoritos.")


def visualizar_favoritos():
    for c in contatos:
        if c["favorito"] == True:
            print(f"Nome: {c['nome']}")
            print(f"Telefone: {c['telefone']}")
            print(f"E-mail: {c['email']}")
            print(f"Favorito: {c['favorito']}")


def apagar_contato():
    visualizar_contatos()
    num = int(input("Informe o número do contato: "))
    if num < 1 or num > len(contatos):
        print("Número não encontrado")
        return

    contato = contatos[num - 1]
    contatos.remove(contato)
    print(f"Contato {contato} removido com sucesso")



while True:
    print("\n-------------- Agenda de contatos --------------")

    print("1. Adicionar contato")
    print("2. Editar contato")
    print("3. Excluir contato")
    print("4. Favoritar contato")
    print("5. Listar contatos")
    print("6. Sair")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        adicionar_contato(contato)
    elif opc == "2":
        editar_contato_existente()
    elif opc == "3":
        apagar_contato()
    elif opc == "4":
        marcar_desmarcar_contato_favorito()
    elif opc == "5":
        visualizar_contatos()
    elif opc == "6":
        print("Até breve!")
        break