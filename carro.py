"""
EX1:
Criar um carro com pelo menos 4 atributos, com 2 metodos
    - Ligar/Desligar
    - Consumir combustivel

EX2:
Criar um classe com ponto cartesiao e um metodo para calcular distancia euclidiana entre 2 pontos

O programa n pode permitir criar um ponto vazio (Sem cordenadas)
"""
class Carro:
    def __init__(self, marca, modelo, combustivel=100):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = combustivel
        self.on_off  = False
    
    def onoff(self, ligar=False):
        if self.combustivel > 0 and ligar:
            self.on_off = True
            print('O carro ligou')
        else:
            self.on_off = False

    def acelerar(self):
        if self.on_off:
            _tanque = self.combustivel
            while _tanque > 0:
                print(f'O {self.marca} {self.modelo} esta com {_tanque}% do tanque cheio')
                _tanque = _tanque - 10
            print('Acabou o combustivel')
        else:
            print('Ligue o carro para acelerar!')
            
kicks = Carro('Nissan', 'kicks')
kicks.onoff(True)
kicks.acelerar()