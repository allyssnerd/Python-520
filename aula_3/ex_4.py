
import pymongo

client = pymongo.MongoClient()
db = client.projeto

def buscar_usuario(email):
    u = db.usuarios.find_one({ 'email': email })
    if not u:
        return None
    return u

def cadastrar_usuario(email):
    db.usuarios.insert({
        'nome': input('Digite seu nome: '),
        'idade': input('Digite sua idade: '),
        'email': email
    })
    return buscar_usuario(email)

def perguntar_time():
    return input('Digite o nome do seu time: ')

def cadastrar_torcedor(usuario, time):
    usuario['time'] = time
    db.usuarios.update({ 'email': usuario['email'] }, usuario)

if __name__ == '__main__':

    email = input('Digite seu email: ')

    usuario = buscar_usuario(email)
    
    if not usuario:
        usuario = cadastrar_usuario(email)

    time = perguntar_time()

    cadastrar_torcedor(usuario, time)
