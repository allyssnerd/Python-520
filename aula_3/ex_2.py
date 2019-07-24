
import os

import dotenv

import psycopg2
import psycopg2.extras

dotenv.load_dotenv('.')

conn = psycopg2.connect(
  dbname='projeto', 
  user='admin', 
  password=os.getenv('DATABASE_PASSWORD'),
  host='localhost',
  port='5432'
)

cursor = conn.cursor(
    cursor_factory=psycopg2.extras.RealDictCursor
)

def listar_times():
    query = '''

        SELECT * FROM times;

    '''
    cursor.execute(query)
    return cursor.fetchall()

def cadastrar_torcedor(torcedor, time):
    query = '''

        INSERT INTO rel_usuarios_times (usuario, time)        
        VALUES ({}, {});

    '''.format(torcedor, time)
    cursor.execute(query)
    conn.commit()

def listar_usuarios(email):
    query = '''

        SELECT * FROM usuarios
        WHERE email = '{}';

    '''.format(email)
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':

    email = input('Digite seu email: ')
    resultado = listar_usuarios(email) 

    usuario = None
    if len(resultado) > 0:
        usuario = resultado[0]

    for time in listar_times():
        print('{} - {}'.format(time['id'], time['nome']))
        
    time_selecionado = input(
        'Selecione o time do sz do Goku: '
    )

    cadastrar_torcedor(usuario['id'], time_selecionado)