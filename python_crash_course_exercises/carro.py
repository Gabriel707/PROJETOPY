
class Carro():

    carros = []

    def __init__(self, marca, modelo, ano, cambio, carroceria, cor, vendido=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cambio = cambio
        self.carroceria = carroceria
        self.cor = cor
        self.vendido = vendido

        Carro.carros.append(self)

    def __str__():
        return f'{self.marca} | {self.modelo} | {self.ano} | {self.cambio} | {self.carroceria} | {self.cor} | {self.vendido}'

    def list_carro():
        for carro in Carro.carros:
            print(f"{carro.marca} | {carro.modelo} | {carro.ano} | {
                  carro.cambio} | {carro.carroceria} | {carro.cor} | Vendido: {carro.vendido}")


meu_carro = Carro('Mercedes', 'A250', '2019',
                  'AWD' 'Hatch', 'Branco', '45.000')

meu_carro = Carro('Volvo', 'v40', '2020', 'auto', 'hatch', 'preto', '0')

Carro.list_carro()
