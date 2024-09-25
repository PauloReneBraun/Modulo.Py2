def meu_decorador(func):
    def wrapper():
        print('Estou antes da execução da função')
        func()
        print('Estou depois da execução da função')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Estou sendo executada')

minha_funcao()

class MeuDecorador:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Estou antes da execução da função')
        self.func()
        print('Estou depois da execução da função')

@MeuDecorador
def segunda_funcao():
    print('Estou sendo executada')