
class QuebrandoFlake():
    def __init__(self):
        self.__teste = "quebrando flake"
    def METODO_ERRADO(self):
        self.__teste = "quebrando flake"
        print(self.__teste)
if __name__ == '__main__':
    quebrando = QuebrandoFlake()
    print(quebrando.METODO_ERRADO())