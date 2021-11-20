
class Bola:

    def __init__(self,Cor, Circunferencia,Material):
        self.Cor = Cor
        self.Circunferencia =Circunferencia
        self.Material = Material

    def MudarCor(self,Cor):
        self.Cor = Cor

    def MostrarCor(self):
        print("A cor da bola é : {}" .format(self.Cor))


bola1 = Bola("Azul",60,"Borracha")
bola1.MostrarCor()
bola1.MudarCor("Rosa")
bola1.MostrarCor()
