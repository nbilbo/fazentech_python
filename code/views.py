# coding: utf-8

"""
Não tente entender esses códigos, confesso que ficou confuso.
"""

from tkinter import Frame, Toplevel, Button
from tkinter.ttk import Treeview

from formularios import FormularioFuncionario, FormularioAtulizarFuncionario
from formularios import FormularioAnimal, FormularioAtualizarAnimal
from formularios import FormularioOrdenha, FormularioAtualizarOrdenha

from utils import get_tk


class View(Frame):
    formulario_adicionar = None
    formulario_atualizar = None
    

    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.set_parent(parent)

        # ---criando a tabela
        frame_tabela = Frame(self)
        frame_tabela.pack(fill="both", expand=True)
        frame_tabela.pack_propagate(False)

        self.tabela = Treeview(frame_tabela)
        self.tabela.column("#0", width=0, minwidth=0, stretch=False)
        self.tabela.pack(fill="both", expand=True)

        # ---criando os botoes
        frame_botoes = Frame(self)
        frame_botoes.pack(fill="x")

        self.botao_adicioanar = Button(frame_botoes, text="Adicioanar")
        self.botao_atualizar = Button(frame_botoes, text="Atualizar")
        #self.botao_remover = Button(frame_botoes, text="Remover")

        self.botao_adicioanar["command"] = self.abrir_formulario_adicionar
        self.botao_atualizar["command"] = self.abrir_formulario_atualizar
        #self.botao_remover["command"] = self.remover_dados

        for botao in (self.botao_adicioanar, self.botao_atualizar):
            botao.pack(side="left", fill="x", expand=True, padx=5, pady=5)
    
    def abrir_formulario_adicionar(self):
        """
        Instanciar um novo formulario p/ inserir os dados.
        """
        if self.formulario_adicionar:
            novo_formulario = self.formulario_adicionar(parent=self)
            # carregadando o estilo
            programa = get_tk(self)
            programa.carregar_estilo(novo_formulario, "button")
            programa.carregar_estilo(novo_formulario, "label")
            programa.carregar_estilo(novo_formulario, "entry")
            
    
    def abrir_formulario_atualizar(self):
        """
        Instanciar um novo formulario p/ atualizar os dados.
        """
        if self.formulario_atualizar:
            selecoes = self.tabela.selection()
            if selecoes:
                _id = str(self.tabela.item(selecoes[0])["values"][0])
                novo_formulario = self.formulario_atualizar(parent=self, id=_id)
                # carregadando o estilo
                programa = get_tk(self)
                programa.carregar_estilo(novo_formulario, "button")
                programa.carregar_estilo(novo_formulario, "label")
                programa.carregar_estilo(novo_formulario, "entry")
        
    def remover_dados(self):
        """
        Apagar as informacoes da linha selecionada.
        """
        pass
    
    def atualizar_tabela(self):
        """
        Buscar os dados no arquivo json p/ atualizar as linhas da tabela.
        """
        pass
            
    
    def limpar_tabela(self):
        """
        Remover todas as linhas a tabela.
        """
        self.tabela.delete(*self.tabela.get_children())

    def set_parent(self, parent):
        self.parent = parent
    
    def get_parent(self):
        return self.parent
    
    def get_dados(self):
        """
        Retornar um dicionario python do arquivo json (dados.json).
        """
        #programa = self.get_parent()
        programa = get_tk(self)
        return programa.get_dados()
    
    def get_selecao(self):
        """
        Retornar a linha atual selecionada
        """
        selecoes = self.tabela.selection()
        return selecoes[0] if len(selecoes) else []


class ViewFuncionarios(View):
    formulario_adicionar = FormularioFuncionario
    formulario_atualizar = FormularioAtulizarFuncionario

    def __init__(self, *args, **kwargs):
        super(ViewFuncionarios, self).__init__(*args, **kwargs)
        # configurando a tabela
        self.tabela["columns"] = ["id", "nome"]
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.column("id", width=50, minwidth=50, stretch=False)
    
    def atualizar_tabela(self):
        """
        Atualizar a tabela de funcionários.
        """
        self.limpar_tabela()
        funcionarios = self.get_dados()["funcionários"]
        for _id, informacoes in funcionarios.items():
            self.tabela.insert("", "end", values=(_id, informacoes["nome"]))

    def remover_dados(self):
        linha = self.get_selecao()
        if linha:
            id_funcionario = str(self.tabela.item(linha)["values"][0])
            get_tk(self).remover_dados(id_funcionario, "funcionários")    


class ViewAnimais(View):
    formulario_adicionar = FormularioAnimal
    formulario_atualizar = FormularioAtualizarAnimal

    def __init__(self, *args, **kwargs):
        super(ViewAnimais, self).__init__(*args, **kwargs)
        # configurando a tabela
        self.tabela["columns"] = ["id", "raca", "peso"]
        self.tabela.heading("id", text="ID")
        self.tabela.heading("raca", text="Raça")
        self.tabela.heading("peso", text="Peso (Kg)")
        self.tabela.column("id", width=50, minwidth=50, stretch=False)
    
    def atualizar_tabela(self):
        """
        Atualizar a tabela de animais.
        """
        self.limpar_tabela()
        animais = self.get_dados()["animais"]
        for _id, informacoes in animais.items():
            self.tabela.insert("", "end", 
                            values=(_id, informacoes["raça"], informacoes["peso"]))

    def remover_dados(self):
        linha = self.get_selecao()
        if linha:
            id_animal = str(self.tabela.item(linha)["values"][0])
            get_tk(self).remover_dados(id_animal, "animais")    


class ViewOrdenhas(View):
    formulario_adicionar = FormularioOrdenha
    formulario_atualizar = FormularioAtualizarOrdenha

    def __init__(self, *args, **kwargs):
        super(ViewOrdenhas, self).__init__(*args, **kwargs)
        # configurando a tabela
        self.tabela["columns"] = ["id", "funcionario", "quantidade"]
        self.tabela.heading("id", text="ID")
        self.tabela.heading("funcionario", text="Funcionário")
        self.tabela.heading("quantidade", text="Quantidade (Litros)")
        self.tabela.column("id", width=50, minwidth=50, stretch=False)
        self.tabela.column("quantidade", width=150, minwidth=150, stretch=False)
    
    def atualizar_tabela(self):
        """
        Atualizar a tabela.
        """
        self.limpar_tabela()
        ordenhas = self.get_dados()["ordenhas"]
        funcionarios = self.get_dados()["funcionários"]
        

        for id_ordenha, ordenha in ordenhas.items():
            # procurando pelo nome do funcionario
            funcionario_nome = [funcionario["nome"] for id_funcionario, funcionario in funcionarios.items() if id_funcionario == ordenha["funcionário"]]
            funcionario_nome = funcionario_nome[0] if len(funcionario_nome) else "Não encontrado"
            self.tabela.insert("", "end", values=(id_ordenha, funcionario_nome, ordenha["litros"]))

    def remover_dados(self):
        """
        Remover a linha selecionada do arquivo json.
        """
        linha = self.get_selecao()
        if linha:
            id_ordenha = str(self.tabela.item(linha)["values"][0])
            get_tk(self).remover_dados(id_ordenha, "ordenhas")    
