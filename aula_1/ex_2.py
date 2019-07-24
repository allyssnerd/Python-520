
usuario = {
    'nome': 'Belzebu',
    'email': 'bel@zebu.com',
    'idade': input('Digite sua idade: ')
}

'''
condicao = 10 > 50

if condicao:
    print('Verdade')
    print('Lucas Ricciardi de Salles')
else:
    print('Falso')    

print('Sempre imprime isso')
'''

if not usuario['idade'].isnumeric():
    exit()
print('Opa ta ok')

idade = int(usuario['idade'])

if (idade / 5) > 1200:
    print('Você é velho')
else:
    print('Você é jovem')


if '@' not in usuario['email']:
    print('Email inválido')
else:
    print('Tudo ok')

score = 77


if score < 33.3:
    color = 'red' 
elif score < 66.6:
    color = 'yellow'
else:
    color = 'green'
