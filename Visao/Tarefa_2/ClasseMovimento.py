from ClasseMotor import Motor

class Movimento:

    motor1 = Motor(1)
    motor2 = Motor(2)

    def Frente(self,velocidade = 100):
        self.motor1.Velocidade = velocidade
        self.motor2.Velocidade = velocidade

    def Tras(self,velocidade = 100):
        self.motor1.Velocidade = -velocidade
        self.motor2.Velocidade = -velocidade

    def Girar(self,sentido = "DIREITA",velocidade = 100):

        if sentido.upper() == "DIREITA":

            self.motor1.Velocidade = -velocidade
            self.motor2.Velocidade = velocidade
        elif sentido.upper() == "ESQUERDA":

            self.motor1.Velocidade = velocidade
            self.motor2.Velocidade = -velocidade
        else:
            self.motor1.MudarVelocidade()
            self.motor2.MudarVelocidade()

    def Parar(self):
        self.motor1.MudarVelocidade()
        self.motor2.MudarVelocidade()


movimento1 = Movimento()

movimento1.Frente()
print("Velocidade motor 1 :{} /  motor 2:{}".format(movimento1.motor1.Velocidade,movimento1.motor2.Velocidade))
movimento1.Tras()
print("Velocidade motor 1 :{} /  motor 2:{}".format(movimento1.motor1.Velocidade,movimento1.motor2.Velocidade))
movimento1.Girar("direita")
print("Velocidade motor 1 :{} /  motor 2:{}".format(movimento1.motor1.Velocidade,movimento1.motor2.Velocidade))
movimento1.Girar("esquerda")
print("Velocidade motor 1 :{} /  motor 2:{}".format(movimento1.motor1.Velocidade,movimento1.motor2.Velocidade))
movimento1.Parar()
print("Velocidade motor 1 :{} /  motor 2:{}".format(movimento1.motor1.Velocidade,movimento1.motor2.Velocidade))

