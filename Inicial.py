import PySimpleGUI as sg
import sqlite3 as lite
from tkinter import *
from datetime import datetime

sg.theme('DarkBlue13')

# -------------------- View ---------------------
def janela_Inicio():
    layout = [
        [sg.Button('Login', size=(20, 5)), sg.Button('Cadastro', size=(20, 5))]
    ]

    layout_Inicio = [
        [sg.Column(layout, vertical_alignment='c', justification='c')] # 'c' utilizado em justification se refere ao centro de forma horizontal, vertical_alignment não esta funcionando 
    ]                                                                  # mas teria o mesmo intuito.
    return sg.Window('Inicio', size=(400, 350), layout=layout_Inicio, finalize=True)

def janela_SignUp():
    
    layout = [
        [sg.Text('Nome :')],
        [sg.Input(key='nome', size=(35,0))],
        [sg.Text('Sobrenome :')],
        [sg.Input(key='sobrenome',size=(35,0))],
        [sg.Text('Usuário :')], # Nickname
        [sg.Input(key='usuario',size=(35,0))],
        [sg.Text('Senha :',)],
        [sg.Input(key='senha',password_char='*',size=(35,0))],
        [sg.Text('CPF :')], # Chave Primaria
        [sg.Input(key='cpf',size=(35,0))],
        [sg.Input(key='data cadastro', visible=False)],
        [sg.Button('Cadastrar')]
    ]

    layout_SignUp = [
        [sg.Button('Voltar', size=(6,1))],
        [sg.Column(layout, vertical_alignment='c', justification='c')]
    ]
    return sg.Window('Sign Up', size=(400, 350), layout=layout_SignUp, finalize=True)

def janela_Login():
    layout = [
        [sg.Text('CPF :')],
        [sg.Input(key='cpf',size=(35,0))],
        [sg.Text('Senha:', size=(5,0))],
        [sg.Input(key='senha',password_char='*', size=(35,0))],
        [sg.Button('Login')]
    ]

    layout_Login = [
        [sg.Button('Voltar', size=(6,0))],
        [sg.Column(layout, vertical_alignment='center', justification='c')]
    ]
    return sg.Window('Login', size=(400, 350), layout=layout_Login, finalize=True)

def janela_Perfil():
    layout = [
        #Criar tela com todas as informações e botões de delete e update, os 2 pedem senha para realizar a ação
    ]

    layout_Perfil = [
        [sg.Button('Sair', size=(6,0))],
        [sg.Column(layout, vertical_alignment='center', justification='c')]
    ]
    return sg.Window('Perfil', size=(700, 540), layout=layout_Perfil, finalize=True)

# -------------------- Model --------------------

def create(nome, sobrenome, nickname, senha, cpf):
    con = lite.connect('BIT.db')

    lista = [nome, sobrenome, nickname, senha, cpf, datetime.today().strftime('%m/%d/%Y')]

    with con:
        cur = con.cursor()
        query = "INSERT INTO usuario (nome, sobrenome, nickname, senha, cpf, registro) VALUES (?, ?, ?, ?, ?, ?)" 
        cur.execute(query, lista)

def read():
    con = lite.connect('BIT.db')

    with con:
        cur = con.cursor()
        query = "SELECT * FROM usuario"
        cur.execute(query)
        info = cur.fetchall()
        print(info)

def update(nome, sobrenome, nickname, senha, cpf):
    con = lite.connect('BIT.db')

    lista = [nome, sobrenome, nickname, senha, cpf]

    with con:
        cur = con.cursor()
        query = "UPDATE usuario (nome = ?, sobrenome = ?, nickname = ?, senha = ?) WHERE cpf = ?" 
        cur.execute(query, lista)

def delete(cpf):
    con = lite.connect('BIT.db')
    lista = [cpf]

    with con:
        cur = con.cursor()
        query = "DELETE FROM usuario WHERE cpf=?"
        cur.execute(query, lista)
        read()
        con.commit()

# ----------------- Controller ------------------
janela1, janela2 = janela_Inicio(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'Login':
        janela2 = janela_Login()
        janela1.hide()
    if window == janela1 and event == 'Cadastro':
        janela2= janela_SignUp()
        janela1.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()


    if window == janela2 and event == 'Login':
        if values['cpf'] == '12345678999' and values['senha'] == 'senha1':
            sg.popup("Entrando na conta...")
            janela2.hide()
            janela2 = janela_Perfil

        else:
            sg.popup('Usuario ou senha errados, tente novamente') 

    if window == janela2 and event == 'Cadastrar':
        if len(values['nome']) < 2 or len(values['sobrenome']) < 2 or len(values['usuario']) < 2 or len(values['senha']) < 8 or len(values['cpf']) != 11 :  # Erro no NULL?????
            sg.popup('Os dados não foram preenchidos corretamente, verifique os dados e tente novamente')
        else:
            create(values['nome'], values['sobrenome'], values['usuario'], values['senha'], values['cpf'])
            sg.popup('Usuario criado')
            read()
            janela2.hide()
            janela1.un_hide()

    # -------------- Teste Errado
    # if event == sg.WINDOW_CLOSED:
    #     break
    # if event == 'Login':
    #     print("Login")
    # elif event == 'Sign Up':
    #     print("Sign Up")
    # elif event == 'Enviar':
        # if len(values['cpf']) > 11:
       #     window.Element('cpf').Update(values['cpf'][:-1])
       # else :
            # print("Enviado")    
            # print('cpf')
        
window.Close()