

class Motor:

    def __init__(self, id, velocidade = 0, SentidoGiro = 1):
        self.Id = id
        self.Velocidade = velocidade
        self.SentidoGiro = SentidoGiro

    def MudarId(self,id):

        self.Id = id

    def MudarVelocidade(self,velocidade = 0):
        self.Velocidade = velocidade

    def MudarSentido(self,sentido = 1):
        self.SentidoGiro = sentido
