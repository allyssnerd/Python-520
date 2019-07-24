
def receber_input(mensagem):
    valor = input(mensagem)
    try:
        return int(valor)
    except ValueError:
        print('Número inválido')

def receber_input_2(mensagem):
    while True:
        valor = input(mensagem)
        try:
            return int(valor)
        except ValueError:
            print('Número inválido')

numero = receber_input_2('Digite um número: ')
print('Você digitou o número {}'.format(numero))

exit()

class ErroSaldoInsuficiente(Exception):
    pass

try:
    raise ErroSaldoInsuficiente({
        'saldo': 0.15
    })
except ErroSaldoInsuficiente as err:
    print(err)

exit()

# Exemplo

def fn(index, key, string):

    x = [ 1, 2, 3 ]
    y = { 'nome': 'Lucas' }

    x[index]
    y[key]
    int(string)

    print('DEU TUDO CERTO AQUI')

def capturar_execao(function, *args):
    try:
        function(*args)
    except IndexError:
        print('Capturado erro na conversão para inteiro')
    except ValueError:
        print('Capturado erro ao tentar acessar indice indisponivel na lista')
    except KeyError:
        print('Capturado erro ao tentar acessar chave nao existente no dicionario')
    except Exception:
        print('Erro capturado')

capturar_execao(fn, 2, 'nome', '55')        #ok
capturar_execao(fn, 3, 'nome', '55')        #e1
capturar_execao(fn, 2, 'idade', '55')       #e2
capturar_execao(fn, 2, 'nome', 'lucas')     #e3

# fn(3, 'nome', '55')     # index error
# fn(2, 'idade', '55')    # key error
# fn(2, 'nome', 'lucas')  # value error









