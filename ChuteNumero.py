# Chute o Número
import random
import PySimpleGUI as sg

class ChuteNumero:
    def __init__(self):
        self.valorAleatorio = 0
        self.valorMin = 1
        self.valorMax = 100
        self.tentarNovamente = True

    def Iniciar(self):

        layout = [
            [sg.Text('Seu Chute',size=(30,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40,10))]
        ]

        self.janela = sg.Window('Chute o número!',layout=layout)
        self.GerarNumero()
        try:
            while True:
               
                self.evento, self.valores = self.janela.Read()

                if self.evento == 'Chutar!':
                    self.valorChute = self.valores['ValorChute']
                    while self.tentarNovamente == True:
                        if int(self.valorChute) > self.valorAleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valorChute) < self.valorAleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valorChute) == self.valorAleatorio:
                            self.tentarNovamente = False
                            print('Parabéns você acertou !!!!!')
                            break
        except:
            print('Por favor digitar apenas números!')
            self.Iniciar()

    def GerarNumero(self):
      self.valorAleatorio = random.randint(self.valorMin,self.valorMax)

chute = ChuteNumero()
chute.Iniciar()
