# Simulador de dado
# Simulado o uso de um dado, gereando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6

        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]

    def Iniciar(self):
        
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)

        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                    self.GerarValorDado()
            elif self.eventos == 'Não' or self.eventos =='n':
                    print('Agradecemos a sua participação!')
            else:
                    print('Por favor digitar sim ou não')
        except:
            print('Ocorrreu um erro ao receber sua resposta.')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))       

# Socorro
simulador = SimuladorDado()
simulador.Iniciar()