import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        layout = [
            [sg.Text('E-mail :', size=(7,0))],
            [sg.Input(size=(35,0))],
            [sg.Text('Senha :', size=(7,0))],
            [sg.Input(size=(35,0))],
            [sg.Text('Nome Completo :')],
            [sg.Input(size=(35,0))],
            [sg.Text('Telefone :')],
            [sg.Input(size=(35,0))],
            [sg.Button('Enviar')]
        ]

        janela = sg.Window("Dados do usuário").layout(layout)

        self.button, self.values = janela.read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()