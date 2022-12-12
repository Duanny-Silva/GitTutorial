class Carro():
    def __init__(self):
        self.cor = "laranja"
        self.marca = "corsa"
        self.placa = "DT986756JD"

    def mostrar(self):
        print(f"A cor é: {self.cor}, da marca {self.marca} e placa {self.placa}")


Carro2 = Carro()
Carro2.mostrar()