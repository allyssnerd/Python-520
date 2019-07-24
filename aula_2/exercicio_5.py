
# Criar uma classe Usuario que tenha
# os atributos nome, idade, email
# e os metodos :
# - maior de idade
# - funcionario da 4linux
# - tem moto

class Usuario:

    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def maior_de_idade(self):
        if self.idade > 21:
            return True
        return False
    
    def funcionario_da_4linux(self):
        if '@4linux' in self.email:
            return True
        return False

    def tem_moto(self):
        if self.nome == 'Lucas Ricciardi de Salles':
            return True
        return False

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
idade = int(input('Digite sua idade: '))

usuario = Usuario(nome, email, idade)

print('Olá {}'.format(usuario.nome))

if usuario.maior_de_idade():
    print('Maior de idade')  

if usuario.tem_moto():
    print('Tem moto')

exit()

class Lampada:

    acesa = False

    def pressionar_interruptor(self):
        self.acesa = not self.acesa
    
lampada1 = Lampada()
lampada2 = Lampada()

lampada1.pressionar_interruptor()

print('Lampada 1: ' + str(lampada1.acesa))
print('Lampada 2: ' + str(lampada2.acesa))
