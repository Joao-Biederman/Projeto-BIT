import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        layout = [
            [sg.Text('E-mail:', size=(5,0)),],
            [sg.Input(key='email',size=(35,0))],
            [sg.Text('Senha:', size=(5,0))],
            [sg.Input(key='senha',password_char='*',size=(35,0))],
            [sg.Checkbox('Mantenha-me Conectado')],
            [sg.Button('Enviar')]
        ]

        janela = sg.Window("Dados do usuário").layout(layout)

        self.button, self.values = janela.read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()