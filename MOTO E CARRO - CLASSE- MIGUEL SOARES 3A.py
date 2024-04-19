class Veículo:
def __init__(self, marca, modelo):
   self.marca = marca
   self.modelo = modelo



def frear(self):
    print(f"{self.marca} {self.modelo} o veiculo está freiando")

    def acelerar(self):
        print(f"{self.marca} {self.modelo} o veiculo está em alta velocidade")
        
class Carro(veículo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    def abrir_porta(self):
        print(f"as portas do"){self.marca} {self.modelo} estão abertas.")

class Moto(Veículo)
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    def RL(self):
        print(f"{self.marca} {self.modelo} {self.cilindrada} esta fezendo uma manobra.")

if __name__ == "__main__":
    carro = Carro("Nissan", "R34", "azul")
    print(carro.frear())
    print(carro.acelerar())
    print(carro.abrir_porta())

    moto = Moto("YAMAHA", "R1", "1000")
     print(moto.frear())
     print(moto.acelerar())
     print(moto.rl())

