tarefas = []

while True:
    opcao = input("O que deseja fazer? \n 1.Cadastrar nova tarefa \n 2.Visualizar tarefas cadastradas \n 3.Sair da aplicação \n >> ")
    if opcao == "1":
        print('Você selecionou: "Cadastrar nova tarefa"')
        while True:
            titulo = input("Que título deseja colocar? ").strip()
            if titulo == "":
                print("O título não pode ficar vazio! Digite novamente: ")
            else:
                break
        while True:
            prioridade = input("Qual a prioridade? (Alta, Média ou Baixa) \n").strip()
            if prioridade not in ["Alta", "Média", "Media", "Baixa"]:
                print("Prioridade inválida, digite Alta, Média ou Baixa")
            else:
                break
        descricao = input("Descrição da tarefa: ").strip()
        data_limite = input("Data limite (ex: 25/10/2026): ").strip()
        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "data_limite": data_limite,
            "status": "Pendente"
        }
        tarefas.append(tarefa)
        print("Tarefa cadastrada com sucesso!")
    elif opcao == "2":
        print(tarefas)
    elif opcao == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida, tente de novo")