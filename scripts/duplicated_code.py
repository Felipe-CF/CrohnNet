class CopiandoFlake():
    def __init__(self):
        self.__teste = "quebrando flake"

    def metodo_duplicado(self):
        print(self.__teste)


if __name__ == '__main__':
    quebrando = CopiandoFlake()
    print(quebrando.metodo_duplicado())
