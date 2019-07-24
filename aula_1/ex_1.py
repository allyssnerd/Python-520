
# tipos primitivos
string = 'Lucas'
inteiro = 26
flutuante = 150000.92
booleano = True

# estruturas de dados
tupla = (1, 2, 3, 4)
lista = [ 1, 2, 3, 4 ]
dicionario = {
    'nome': 'Lucas',
    'idade': 26
}

nome = input('Digite seu nome: ')
print(nome)

# ex1: Criar uma estrutura que armazena:
# - Nome, idade, email, sexo, altura, peso

usuario = {
    'nome': input('Digite seu nome: '),
    'idade': input('Digite sua idade: '),
    'email': input('Digite seu email: '),
    'sexo': input('Digite seu sexo: '),
    'altura': input('Digite sua altura: '),
    'peso': input('Digite seu peso: '),
}
print(usuario)

# ex2: Imprimir no terminal SOMENTE
# o nome e a idade digitadas

nome = usuario['nome']
idade = usuario['idade']

print(nome, idade)
