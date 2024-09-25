def meu_decorador(func):
    def wrapper():
        print('Estou antes da execucao da funcao')
        func()
        print('Estou depois da execucao da funcao')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Estou sendo executada X_X')

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Estou antes da execucao da funcao')
        self.func()
        print('Estou depois da execucao da funcao')

@MeuDecoradorDeClasse
def segunda_funcao():
    print('Estou sendo executada x__x')

segunda_funcao()