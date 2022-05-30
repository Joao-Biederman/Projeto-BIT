# importando SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('BIT.db')

#Criação da tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE usuario(nome TEXT, sobrenome TEXT, nickname TEXT, senha TEXT, cpf INTEGER PRIMARY KEY, registro DATE)")