import main

while True:
    print('-- Bem vindo ao Menu --')
    print('1 - Adicionar aluno')
    print('2 - Editar aluno')
    print('3 - Deletar aluno')
    print('4 - Listar todos os alunos')
    print('5 - Sair')
    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        nome = input('digite o nome do aluno: ')
        idade = int(input('digite a idade do aluno: '))
        nota = float(input('digite a nota do aluno: '))
        main.insert(nome, idade, nota)
    elif opcao == '2':
        nome = input('digite o nome do aluno: ')
        idade = int(input('digite a idade do aluno: '))
        nota = float(input('digite a nota do aluno: '))
        matricula = int(input('digite a matricula do aluno: '))
        main.update(nome, idade, nota, matricula)
    elif opcao == '3':
        matricula = int(input("digite a matricula do aluno: "))
        main.delete(matricula)
    elif opcao == '4':
        main.select()
    elif opcao == '5':
        break
    