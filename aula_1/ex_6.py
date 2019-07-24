
def receber_inteiro(mensagem):
    valor = input(mensagem)
    if valor.isnumeric():
        return valor
    print('Número inválido')


def receber_inteiro_2(mensagem):
    valor = ''
    while not valor.isnumeric():
        valor = input(mensagem)
    return int(valor)

usuario = {
    'nome': input('Digite seu nome: '),
    'idade': receber_inteiro('Digite sua idade: '),
    'peso': receber_inteiro('Digite seu peso: '),
}
