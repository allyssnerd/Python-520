
# Escrever um método que calcula a raiz
# de um número
# A raiz quadrada só é definida para numeros
# positivos, logo se o valor for menor do que
# zero levantem uma execessão

def calcular_raiz(x):
    if x < 0:
        raise Exception
    return x ** (0.5)


try:
    numero = int(input('Digite um número: '))
    print(calcular_raiz(numero))
except:
    print('Você digitou um número inválido')

print('FIM DO PROGRAMA')
