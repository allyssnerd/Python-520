
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
  dbname='projeto', 
  user='admin', 
  password='4linux',
  host='localhost',
  port='5432'
)

cursor = conn.cursor(
    cursor_factory=psycopg2.extras.RealDictCursor
)

def cadastrar_usuario(nome, email, idade):
    query = '''

        INSERT INTO usuarios (nome, email, idade)
        VALUES ('{}', '{}', {});

    '''.format(nome, email, idade)
    cursor.execute(query)
    conn.commit()

def listar_usuarios():
    query = '''

        SELECT * FROM usuarios;

    '''
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':

    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    idade = input('Digite sua idade: ')

    cadastrar_usuario(nome, email, idade)

    for usuario in listar_usuarios():
        print(usuario)