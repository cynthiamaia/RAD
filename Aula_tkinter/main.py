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
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preço:")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Adicionar Produtos", command=self.CadastrarProduto)
        self.btnCadastrar.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Atualizar Produtos", command=self.AtualizarProduto)
        self.btnCadastrar.pack()


    def fExibirTela(self):
            try:
                self.treeProdutos.delete(*self.treeProdutos.get_children())
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

    def AtualizarProduto(self):
        try:
            selected_item = self.treeProdutos.selection() #A função selection() retorna uma lista contendo o identificador do item selecionado.
            if not selected_item:
                return
            item = self.treeProdutos.item(selected_item)
            product = item['values']
            product_id = product[0]
            nome =  self.entryNome.get()
            preco = float(self.entryPreco.get())
            self.objBD.update_product(product_id, nome, preco) #método update_product() do objeto objBD para atualizar as informações do produto no banco de dados
            self.fExibirTela()

            self.entryNome.delete(0, tk.END)
            self.entryPreco.delete(0, tk.END)
            print('Produto Atualizado com Sucesso!')        
        except:
          print('Não foi possível fazer a atualização.')
  
janela = tk.Tk() 
product_app = PrincipalBD(janela) 
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("900x700") 
janela.mainloop() 