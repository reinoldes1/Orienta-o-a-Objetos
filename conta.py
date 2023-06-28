class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format (self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor
    
    def saque(self, valor):
        if (valor <= (self.__saldo +self.__limite)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite de sua conta".format(valor))

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite