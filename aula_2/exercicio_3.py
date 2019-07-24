
def E():
    print('E')
    raise Exception()

def D():
    print('D')    

def C():
    print('C')    

def B():
    print('B')
    E()
    D()

def A():
    print('A')
    try:
        B()
    except:
        print('Capturei um erro na A')
    C()

A()