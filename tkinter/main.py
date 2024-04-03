import tkinter as tk
from tkinter import ttk
import modelo as crud

class PrincipalBD():
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.janela = win

        self.treeProdutos = ttk.Treeview(self.janela, 
                                              columns=("Código do Produto",
                                                        "Nome", 
                                                        "Preço"))
        self.treeProdutos.heading("Código do Produto", text="Código do Produto:")
        self.treeProdutos.heading("Nome", text="Nome:")
        self.treeProdutos.heading("Preço", text="Preço:")
        self.treeProdutos.pack()

        self.lblNome = tk.Label(self.janela, text="Nome:")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preço:")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()

janela = tk.Tk()
product_app = PrincipalBD(janela)
janela.title("Bem vindo a aplicação de banco de dados")
janela.geometry("900x700")
janela.mainloop()