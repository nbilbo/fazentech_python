# coding: utf-8


from tkinter import Tk, messagebox
from tkinter.ttk import Notebook

from views import ViewFuncionarios, ViewAnimais, ViewOrdenhas

class Programa(Tk):
    nome_arquivo_json = "dados.json"

    def __init__(self):
        super(Programa, self).__init__()
        self.configuracoes()
        self.inicializar_dados(dados=self.get_dados())

        # ---criando as abas e instanciando as views 
        gerenciador_abas = Notebook(self)
        gerenciador_abas.pack(fill="both", expand=True)

        self.view_funcionaios = ViewFuncionarios(gerenciador_abas)
        self.view_animais = ViewAnimais(gerenciador_abas)
        self.view_ordenhas = ViewOrdenhas(gerenciador_abas)

        gerenciador_abas.add(self.view_funcionaios, text="Funcionários")
        gerenciador_abas.add(self.view_animais, text="Animais")
        gerenciador_abas.add(self.view_ordenhas, text="Ordenhas")

        # ---carregaando os dados nas tabelas.
        self.atualizar_tabelas()
        
    def executar(self):
        """
        Inicializar a janela principal.
        """
        self.mainloop()

    def configuracoes(self):
        """
        Configuração padrão da janela.
        """
        self.title("Fazentech demo")
        self.geometry("500x500+0+0")
        self.minsize(width=500, height=500)     

    def cadastrar(self, informacoes, tabela):
        """
        Cadastrar uma nova informação no arquivo json.
        """
        from os import path
        from json import dumps


        dados = self.get_dados()
        _id = str(len(dados[tabela])+1)
        dados[tabela][_id] = informacoes

        self.inicializar_dados(dados=dados)
        
        self.feedback("Aviso", "Cadastro realizado com sucesso.")
        self.atualizar_tabelas()
    
    def atualizar(self, id, informacoes, tabela):
        """
        Atualizar determinado valor do arquivo json.
        """
        from os import path
        from json import dumps


        dados = self.get_dados()
        dados[tabela][id] = informacoes

        self.inicializar_dados(dados=dados)
        
        self.feedback("Aviso", "Atualização realizado com sucesso.")
        self.atualizar_tabelas()

    def remover_dados(self, id, tabela):
        from os import path
        from json import dumps


        tabelas = {
            "funcionários": self.view_funcionaios,
            "animais": self.view_animais,
            "ordenhas": self.view_ordenhas
        }

        dados = self.get_dados()
        
        del dados[tabela][id]

        current_dir = path.dirname(path.abspath(__file__))
        json_dir = path.join(current_dir, self.nome_arquivo_json)
        with open(json_dir, "w", encoding="utf-8") as f:
            json_dict = dumps(dados, indent=4, ensure_ascii=False)
            f.write(json_dict)
        
        for tabela in tabelas.values():
            tabela.atualizar_tabela()

    def feedback(self, titulo, mensagem):
        """
        Abrir uma mensagem de aviso.
        """
        messagebox.showinfo(titulo, mensagem)

    def atualizar_tabelas(self):
        """
        Atualizar todas as tabelas.
        """
        self.view_funcionaios.atualizar_tabela()
        self.view_animais.atualizar_tabela()
        self.view_ordenhas.atualizar_tabela()

    def inicializar_dados(self, dados=None):
        """
        Inicilizar o arquivo json.
        """
        from os import path, listdir
        from json import dumps

        
        current_dir = path.dirname(path.abspath(__file__))
        json_dir = path.join(current_dir, self.nome_arquivo_json)

        # atualizando o json
        if self.nome_arquivo_json in listdir(current_dir) and dados:
            python_dict = dados

        # json default.
        else:
            python_dict = {"funcionários":{}, "animais":{}, "ordenhas":{}}

        # criando o arquivo json.
        with open(json_dir, "w", encoding="utf-8") as f:
            json_dict = dumps(python_dict, indent=4, ensure_ascii=False)
            f.write(json_dict)

    def get_dados(self):
        """
        Retornar um dicionario python do arquivo json (dados.json).
        """
        from os import path, listdir
        from json import loads


        current_dir = path.dirname(path.abspath(__file__))
        # se existir o arquivo json
        if self.nome_arquivo_json in listdir(current_dir):
            json_dir = path.join(current_dir, self.nome_arquivo_json)
            with open(json_dir, "r", encoding="utf-8") as f:
                python_dict = loads(f.read())
                return python_dict
        # se não existir o arquivo json
        else:
            return None


if __name__ == "__main__":
    programa = Programa()
    programa.executar()
