while True:
    opcao = input("O que deseja fazer? \n 1.Cadastrar nova tarefa \n 2.Visualizar tarefas cadastradas \n 3.Sair da aplicação \n >> ")
    if opcao == "1":
        print('Você selecionou "Cadastrar nova tarefa"')
    elif opcao == "2":
        print('Você selecionou "Visualizar tarefas cadastradas"')
    elif opcao == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida, tente de novo")