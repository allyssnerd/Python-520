
def exemplo_args(*args):
    print(args)
    print(type(args))

def exemplo_args_2(a, b, *args):
    return a + b + sum(args)

print('EXEMPLO DE *ARGS')
exemplo_args(1, 'dois', 3.0, True)
print(exemplo_args_2(2, 2))
print(exemplo_args_2(0, 0, 2, 2))

def exemplo_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

print('EXEMPLO DE *KWARGS')
exemplo_kwargs(a=1, b='Dois', c=3.0, d=True)

def criar_app(**kwargs):
    nome = kwargs.get('nome') or 'nome-default'
    print(nome)

criar_app()
criar_app(nome='Meu app')

def fn(a, b, c, d, e, f, g, h):
    print(a + e)

lista = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
fn(*lista)