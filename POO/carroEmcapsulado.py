class Carro:
    def __init__(self, marca, cor, valor):
        self.__cor = cor
        self.__marca = marca
        self.__valor = valor

    def get_cor(self):
        return self.__cor

    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def get_marca(self):
        return self.__marca

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def get_valor(self):
        return self.__valor

    def set_valor(self, novo_valor):
        self.__valor = novo_valor
        
    def imprimir_valores(self):
        print("Cor:", self.__cor)
        print("Marca:", self.__marca)
        print("Valor:", self.__valor)

carro1 = Carro("Honda", "Prata", 70000)
carro2 = Carro("Toyota", "Preto", 50000)
carro3 = Carro("Volkswagen", "Vermelho", 40000)

carro1.imprimir_valores()
carro2.imprimir_valores()
carro3.imprimir_valores()



