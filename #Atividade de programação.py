#Atividade de programação

# Filas
{filas_proprietários}
# Função para verificar prioridade
def eh_prioritario(idade, gestante, pcd):
    return idade >= 60 or gestante or pcd

# Adicionar cliente
def adicionar_cliente():
    nome = input("Nome: ")
    try:
        idade = int(input("Idade: "))
        gestante = input("É gestante? (s/n): ").lower() == 's'
        pcd = input("É PCD? (s/n): ").lower() == 's'
    except ValueError:
        print("Entrada inválida.")
        return

    cliente = {"nome": nome, "idade": idade, "gestante": gestante, "pcd": pcd}
    if eh_prioritario(idade, gestante, pcd):
        fila_prioritaria.append(cliente)
        print(f"{nome} adicionado à fila prioritária.")
    else:
        fila_normal.append(cliente)
        print(f"{nome} adicionado à fila normal.")

# Atender próximo cliente
def atender_cliente():
    if fila_prioritaria:
        cliente = fila_prioritaria.popleft()
    elif fila_normal:
        cliente = fila_normal.popleft()
    else:
        print("Nenhum cliente na fila.")
        return
    atendidos.append(cliente)
    print(f"Atendido: {cliente['nome']}")

# Listar filas
def listar_filas():
    print("\nFila Prioritária:")
    for c in fila_prioritaria:
        print(f"- {c['nome']} ({c['idade']} anos)")
    print("\nFila Normal:")
    for c in fila_normal:
        print(f"- {c['nome']} ({c['idade']} anos)")

# Relatório
def relatorio():
    total = len(atendidos)
    prioritarios = sum(1 for c in atendidos if eh_prioritario(c['idade'], c['gestante'], c['pcd']))
    print("\n Relatório:")
    print(f"Total atendidos: {total}")
    print(f"Fila prioritária: {len(fila_prioritaria)}")
    print(f"Fila normal: {len(fila_normal)}")
    print(f"% de prioritários atendidos: {(prioritarios / total * 100) if total else 0:.2f}%")

# Menu principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar cliente")
        print("2. Atender próximo")
        print("3. Listar filas")
        print("4. Relatório")
        print("5. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            atender_cliente()
        elif opcao == '3':
            listar_filas()
        elif opcao == '4':
            relatorio()
        elif opcao == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

menu()
