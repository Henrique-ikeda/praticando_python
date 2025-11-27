lista_de_tarefas = []


def iu():
    opcao = 0
    while opcao != 4:
        try:
            print("===GERENCIADOR DE TAREFAS:===")
            print("1. Adicionar tarefa")
            print("2. Visualizar tarefas")
            print("3. Remover tarefa ")
            print("4. Sair")
            opcao = int(input("Escolha uma opção:"))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                visualizar_tarefa()
            elif opcao == 3:
                remover_tarefa()
            elif opcao >= 5:
                print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
        except Exception as e:
            print(f"Ocorreu um erro:{e}")
            iu()
    print("Saindo do gerenciador de tarefas. Até mais!")


def adicionar_tarefa():
    tarefa = input("Digite a tarefa:")
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada!")


def visualizar_tarefa():
    if lista_de_tarefas:
        print("Tarefas:")
        num = 1
        for tarefa in lista_de_tarefas:
            print(f"{num}. {tarefa}")
            num += 1
    else:
        print("A lista está vazia adicione algo na lista")


def remover_tarefa():
    try:
        item_remover = int(input("Digite o número da tarefa a ser removida:"))
        lista_de_tarefas.remove(lista_de_tarefas[item_remover-1])
        print(f"Tarefa {lista_de_tarefas[item_remover-1]} removida!")
    except Exception as e:
        print(f"Erro: Entrada inválida! Digite um número.")
        remover_tarefa()
    except ValueError:
        print("Erro: Nenhuma tarefa para remover.")
