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
    
    def __verifica_saque(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel)

    def saque(self, valor):
        if (self.__verifica_saque(valor)):
            self.__saldo -= valor
        else:
            soma = valor - (self.__saldo + self.__limite)
            print("O valor R${} está R${} acima do limite (R${}) da sua conta".format(valor, soma, (self.__limite + self.__saldo)))

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

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos_externos():
        return {'BB':'001', 'Caixa':"104", "Bradesco":'237', 'Itau':'341'}