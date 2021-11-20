from transitions import Machine
import random

class Universitarios(object):

    # Estados
    states = ['dormindo', 'estudando', 'no bar', 'sair', 'fome','pleno']

    def __init__(self, name):


        self.name = name

        # materias estudadas
        self.materias = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=Universitarios.states, initial='dormindo')

        # transições

        # acordando
        self.machine.add_transition(trigger='acordar', source='dormindo', dest='fome')

        # comer
        self.machine.add_transition('comer', 'fome', 'pleno')

        # estudar
        self.machine.add_transition('estudar', 'pleno', 'estudando')

        # ir pro bar
        self.machine.add_transition('stress', '*', 'no bar',
                         before='chamar_amigos')

        # voltar casa
        self.machine.add_transition('voltar', 'no bar', 'dormindo',
                         after='arrependimento')

        
        self.machine.add_transition('surtar', 'estudando', 'no bar', conditions=['surtando'])
        self.machine.add_transition('surtar', '*', 'no bar')


        self.machine.add_transition('dormir', '*', 'dormindo')

    def arrependimento(self):
        print("Nunca mais eu bebo denovo!!")

    @property
    def surtando(self):

        return  random.random()< 0.5

    def chamar_amigos(self):
        print("{}: Ow ninguem quer ir pro Bar hj a noite n? mó vontade de tomar uma <insert emoji here>".format(self.name))

paulo = Universitarios("Paulo")
print(paulo.state)

paulo.acordar()
print(paulo.state)

paulo.comer()
print(paulo.state)

paulo.estudar()
print(paulo.state)

paulo.stress()
print(paulo.state)

paulo.voltar()
print(paulo.state)

paulo.acordar()
print(paulo.state)

paulo.surtar()
print(paulo.state)