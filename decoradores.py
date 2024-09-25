def meu_decorador(func):
    def wrapper():
        print('Estou antes da execução da função')
        func()
        print('Estou depois da execução da função')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Estou sendo executada')