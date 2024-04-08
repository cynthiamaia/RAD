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
                                                        "Preço"),
                                              show="headings") 
   
        self.treeProdutos.heading("Código do Produto", text="Código do Produto:")
        self.treeProdutos.heading("Nome", text="Nome:")
        self.treeProdutos.heading("Preço", text="Preço:")
        self.treeProdutos.pack()

        self.fExibirTela()

        self.lblNome = tk.Label(self.janela, text="Nome:")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        #self.entryNome = tk.Entry(self.janela,width=60)
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preço:")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Adicionar Produtos", command=self.CadastrarProduto)
        self.btnCadastrar.pack()


    def fExibirTela(self):
            try:
                products = self.objBD.select_all_products() 
                for product in products:
                    self.treeProdutos.insert("", tk.END, values=product)
            except:
                print('Não foi possível exibir os campos.')

    def CadastrarProduto(self):
        try:
            name = self.entryNome.get()
            price = float(self.entryPreco.get())
            self.objBD.inserirDados(name, price)
            self.fExibirTela()

            self.entryNome.delete(0, tk.END)
            self.entryPreco.delete(0, tk.END)
            print('Produto Cadastrado com Sucesso!')
        except:
             print('Não foi possível fazer o cadastro.')

    
  
janela = tk.Tk() 
product_app = PrincipalBD(janela) 
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("900x700") 
janela.mainloop() 