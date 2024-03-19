import sqlite3
from modelo import Pessoa, Marca, Veiculo
banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(
                cpf INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL
                );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY(id)           
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY(placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id));''')

"""cursor.execute('''ALTER TABLE 
               Veiculo ADD motor 
               REAL;''')"""

"""
###uma das formas
#criar uma classe Pessoa
#criar objeto do tipo Pessoa
pessoa = Pessoa(92345678900, 
                'Pedro', '2000-01-31',
                True)
#Inserção de dados em tabela com query dinâmicas
comando = '''INSERT INTO Pessoa 
(cpf, nome, nascimento, oculos) 
VALUES (?, ?,?,?);''' #delimitador “?”
cursor.execute(comando, (pessoa.cpf,
                         pessoa.nome, 
                         pessoa.nascimento,
                         pessoa.usa_oculos))

"""
"""
###
##Outra forma
# Cria uma lista de objetos Pessoa
pessoas = [
    Pessoa(12345678900, 'João', '2000-01-31', True),
    Pessoa(98765432100, 'Cynthia', '1995-03-10', False)
]

# Inserção de dados em tabela com query dinâmicas usando executemany
comando = '''INSERT INTO Pessoa (cpf, nome, 
nascimento, oculos) VALUES (?, ?,?,?);'''
cursor.executemany(comando,
                   [(i.cpf, i.nome, 
                    i.nascimento, 
                    i.usa_oculos) 
                    for i in pessoas])
"""