while True:
    opcao = input("O que deseja fazer? \n 1.Cadastrar nova tarefa \n 2.Visualizar tarefas cadastradas \n 3.Sair da aplicação \n >> ")
    if opcao == "1":
        print('Você selecionou "Cadastrar nova tarefa"')
        while True:
            titulo = input("Que título deseja colocar? ").strip()
            if titulo == "":
                print("O título não pode ficar vazio, digite de novo")
            else:
                break
        while True:
            prioridade = input("Qual a prioridade? (Alta, Média ou Baixa) ").strip()
            if prioridade not in ["Alta", "Média", "Media", "Baixa"]:
                print("Prioridade inválida, digite Alta, Média ou Baixa")
            else:
                break
        print("Tarefa cadastrada com sucesso!")
        print("Título:", titulo)
        print("Prioridade:", prioridade)
    elif opcao == "2":
        print('Você selecionou "Visualizar tarefas cadastradas"')
    elif opcao == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida, tente de novo")