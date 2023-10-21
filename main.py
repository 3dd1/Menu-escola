# pymysql

import pymysql.cursors

try:
    conexao = pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='escola',
                          cursorclass=pymysql.cursors.DictCursor)
    print('Conexão estabelecida com sucesso!')
except Exception as erro:
    print(f'Error ao conectar com o banco: {erro}')

cursor = conexao.cursor()

def select():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(f'Nome: {aluno["nome"]} - Nota: {aluno["nota"]}')
    except Exception as error:
        print(f'Error ao buscar: {error}')

# select()
def insert(nome, idade, nota):
    try:
        sql = f"INSERT INTO alunos (nome, idade, nota)" \
              "VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, idade, nota))
        conexao.commit()
        print('dados cadastrados com sucesso!')
    except Exception as error:
        print(f'erro ao cadastrar: {error}')
#insert("Luan Lopes", 23, 9.5)
# select()

def update(nome, idade, nota, matricula):
    try:
        sql = "UPDATE alunos SET nome = %s, idade = %s," \
              "nota = %s WHERE matricula = %s"
        cursor.execute(sql, (nome, idade, nota, matricula))
        conexao.commit()
        print('Dados alterados com sucesso!')
    except Exception as error:
        print(f'Error ao atualizar os dados: {error}')
# update('Leticia Mota', 25, 9.7, 1)

def delete(matricula):
    try:
        sql = "DELETE FROM alunos WHERE matricula = %s"
        cursor.execute(sql, (matricula))
        conexao.commit()
        print('Aluno deletado com sucesso!')
    except Exception as error:
        print(f'Erro ao deletar aluno: {error}')
# delete()
# select()

def alunoExiste(matricula):
    try:
        if alunoExiste(matricula):
            sql = "SELECT * FROM alunos WHERE matricula = %s"
            cursor.execute(sql, matricula)
            conexao.commit()
            print('Aluno encontrado com sucesso!')
        else:
            print('aluno não encontrado!')
    except Exception as error:
        print(f'Erro ao consultar dados: {error}')
delete(2)
delete(2)