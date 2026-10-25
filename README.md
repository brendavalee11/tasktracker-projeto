# TaskTracker

## Descrição
O TaskTracker é uma aplicação de linha de comando (CLI) para gerenciar tarefas do dia a dia. Com ele, o usuário pode cadastrar tarefas e visualizar a lista de tarefas cadastradas!

Cada tarefa possui:
- Título (obrigatório)
- Descrição
- Prioridade (Alta, Média ou Baixa)
- Data limite
- Status (definido automaticamente como "Pendente" no cadastro)

## Tecnologias
- Python 3
- Git e GitHub

## Instalação
1. Tenha o Python 3 instalado. Para conferir, abra o terminal e rode `python --version`.
2. Baixe o projeto com o comando:

```
git clone https://github.com/brendavalee11/tasktracker-projeto.git
```

## Como executar
1. Abra o terminal na pasta do projeto:

```
cd tasktracker-projeto
```

2. Execute o comando:

```
python src/main.py
```

3. Use o menu para cadastrar tarefas, visualizá-las ou sair.

## Executando com Docker

Para rodar com Docker, é preciso ter o Docker Desktop instalado e aberto.

Como construir a imagem:

```
docker build -t tasktracker .
```

Como rodar o container em modo isolado:

```
docker run -it tasktracker
```

Como rodar via orquestração (Recomendado):

```
docker compose run tasktracker-app
```

O `docker-compose.yml` mantém a entrada do teclado aberta (`stdin_open`) e liga um terminal virtual (`tty`), o que permite usar o menu da aplicação dentro do container.