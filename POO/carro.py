class Carro:
  
    def __init__(self, modelo, cor, marca, valor):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.valor = valor

    def imprimir_valores(self):
        print("Modelo:", self.modelo)
        print("Cor:", self.cor)
        print("Marca:", self.marca)
        print("Valor:", self.valor)

carro1 = Carro("Civic", "Prata", "Honda", 70000)
carro2 = Carro("Corolla", "Preto", "Toyota", 50000)
carro3 = Carro("Gol", "Vermelho", "Volkswagen", 40000)

carro1.imprimir_valores()