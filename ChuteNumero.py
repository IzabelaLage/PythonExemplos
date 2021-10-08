# Chute o Número
import random

class ChuteNumero:
    def __init__(self):
        self.valorAleatorio = 0
        self.valorMin = 1
        self.valorMax = 100
        self.tentarNovamente = True

    def Iniciar(self):
        self.GerarNumero()
        self.PedirValorAleatorio()
        try:
            while self.tentarNovamente == True:
                if int(self.valorChute) > self.valorAleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valorChute) < self.valorAleatorio:
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                if int(self.valorChute) == self.valorAleatorio:
                    self.tentarNovamente = False
                    print('Parabéns você acertou !!!!!')
        except:
            print('Por favor digitar apenas números!')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valorChute = input('Chute um número: ')


    def GerarNumero(self):
      self.valorAleatorio = random.randint(self.valorMin,self.valorMax)

chute = ChuteNumero()
chute.Iniciar()
