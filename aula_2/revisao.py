
# Escrever uma função chamado maximo que 
# recebe três números e retorna qual deles 
# é o MAIOR

def maximo(a, b, c):
    return max(a, b, c)

res = maximo(1, 2, 3)
print(res)

# escrever uma função mult_lista
# que recebe uma lista de números
# e retorna a multiplicacao deles todos

# ex: mult_lista([ 1, 2, 3, 4 ])

def mult_lista(lista_de_numeros):
    resultado = 1
    for numero in lista_de_numeros:
        resultado = resultado * numero
    return resultado

resultado = mult_lista([ 1, 2, 3, 4, 5, 6 ])
print(resultado)

# Escrever uma função que recebe uma string
# (um nome por exemplo) e retorna o número
# caracters minusculos e o numero de caracters
# maiusculos, chame ela de contador

def contador(string):
    maisculas, minusculas = [], []
    for token in string.replace(' ', ''):
        if token.islower():
            minusculas.append(token)
        else:
            maisculas.append(token)
    return maisculas, minusculas

meu_nome = 'Lucas Ricciardi de Salles'
maisculas, minusculas = contador(meu_nome)
print(maisculas, len(maisculas))



















