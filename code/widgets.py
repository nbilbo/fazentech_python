# coding: utf-8

from datetime import datetime

from tkinter import (Frame, Toplevel, Label, Entry, LabelFrame,
                    Radiobutton, StringVar, OptionMenu, Button,
                    Spinbox, Scale, IntVar)
from tkinter.ttk import Treeview

from utils import get_tk
from maskedentry import MaskedWidget


####
# ---widgets 
####
class Widget(LabelFrame):
    def __init__(self, parent, label):
        super(Widget, self).__init__(parent)
        self.set_parent(parent)
        self.config(text=label, borderwidth=2,)
    
    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent


class NormalInput(Widget):
    def __init__(self, parent, label):
        super(NormalInput, self).__init__(parent, label)
        self.input = Entry(self)

        # posicionando
        self.input.pack(side="left", fill="x", expand=True, padx=5, pady=5)
    
    def get_input(self):
        """
        Retornar um valor do campo.
        """
        return self.input.get()
    
    def set_input(self, input):
        self.input.delete(0, "end")
        self.input.insert("end", input)


class GeneroInput(Widget):
    def __init__(self, parent, label):
        super(GeneroInput, self).__init__(parent, label)
        # criando os widgets
        self.var_genero = StringVar()
        self.radio_masc = Radiobutton(self, text="Masculino", value="masculino", 
                                                        variable=self.var_genero)
        self.radio_femi = Radiobutton(self, text="Feminino", value="feminino", 
                                                    variable=self.var_genero)
        self.var_genero.set("masculino")

        # posicionando 
        self.radio_masc.pack(side="left", padx=5, pady=5)
        self.radio_femi.pack(side="right", padx=5, pady=5)
    
    def get_genero(self):
        """
        Retornar o valores selecionado.
        """
        return self.var_genero.get()
    
    def set_genero(self, genero):
        self.var_genero.set(genero)
       

class MenuOpcoes(Widget):
    def __init__(self, parent, label, valores):
        super(MenuOpcoes, self).__init__(parent, label)
        # criando os widgets
        self.string_var = StringVar()
        self.string_var.set(valores[0])
        self.menu = OptionMenu(self, self.string_var, *valores)

        # posicionando
        self.menu.pack(fill="x", expand=True, padx=5, pady=5)
    
    def set_valores(self, valores):
        """
        Atualizar os valores do menu.
        """
        self.menu.children["menu"].delete(0, "end")
        self.string_var.set(valores[0])
        for valor in valores:
            self.menu.children["menu"].add_command(label=valor, 
                                        command=lambda string=valor: self.string_var.set(string))
    
    def get_opcao(self):
        """
        Retornar a opção selecionada.
        """
        return self.string_var.get()

    def get_string_var(self):
        """
        Retornar o atributo string_var. (Para fazer algum trace, por exemplo.)
        """
        return self.string_var


class EnderecoInput(Widget):
    def __init__(self, parent, label):
        super(EnderecoInput, self).__init__(parent, label)
        # ---carregando os estados
        estados = [estado["Nome"] for estado in self.get_estados()]

        # ---carregando as cidades 
        cidades = [cidade["Nome"] for cidade in self.get_cidades() if cidade["Estado"]=="1"]

        # ---criando o menu dos estados
        self.menu_estados = MenuOpcoes(self, label="Estado", valores=estados)
        # chamar o método sempre que for alterado o valor do menu.
        self.menu_estados.get_string_var().trace("w", self.menu_estados_alterado)
        
        # ---criando o menu das cidades
        self.menu_cidades = MenuOpcoes(self, label="Cidade", valores=cidades)

        # ---posicionando
        self.menu_estados.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        self.menu_cidades.pack(side="left", fill="x", expand=True, padx=5, pady=5)
    
    def menu_estados_alterado(self, *args, **kwargs):
        """
        Atualizar o menu_cidades com valores referente ao estado atual.
        """
        estado = self.get_id_estado()
        cidades = [cidade["Nome"] for cidade in self.get_cidades() if cidade["Estado"]==estado]
        self.menu_cidades.set_valores(cidades)
        
    def get_estados(self):
        """
        Retornar um dicionario python do arquivo json 
        (cidades-estados-brasil-json/Estados.json).
        """
        from os import path
        from json import loads


        current_dir = path.dirname(path.abspath(__file__))
        estados_dir = path.join(current_dir, "cidades-estados-brasil-json", "Estados.json")
        with open(estados_dir, "r", encoding="utf-8") as f:
            return loads(f.read())
    
    def set_estado(self, estado):
        """
        Definir o estado que vai ficar selecionado no menu de opcoes.
        """
        self.menu_estados.get_string_var().set(estado)
    
    def get_cidades(self):
        """
        Retonar um dicionario python do arquivo json 
        (cidades-estados-brasil-json/Cidades.json).
        """
        from os import path
        from json import loads


        current_dir = path.dirname(path.abspath(__file__))
        cidades_dir = path.join(current_dir, "cidades-estados-brasil-json", "Cidades.json")
        with open(cidades_dir, "r", encoding="utf-8") as f:
            return loads(f.read())
    
    def set_cidade(self, cidade):
        """
        Definir a cidade que vai ficar selecionado no menu de opcoes.
        """
        self.menu_cidades.get_string_var().set(cidade)

    def get_id_estado(self):
        """
        Retornar o id do estado referente ao arquivo json.
        """
        nome_estado_atual = self.menu_estados.get_opcao()
        for estado in self.get_estados():
            if estado["Nome"] == nome_estado_atual:
                return estado["ID"]
    
    def get_endereco(self):
        """
        Retornar os valores de todos os campos.
        """
        valores = {}
        valores["estado"] = self.menu_estados.get_opcao()
        valores["cidade"] = self.menu_cidades.get_opcao()
        return valores


class ContatoInput(Widget):
    """
    Uma tabela p/ adicionar e remover vários números de telefone.
    """
    def __init__(self, parent, label):
        super(ContatoInput, self).__init__(parent, label)
        # ---criando o campo de entrada de dados
        frame_entrada = Frame(self)

        self.input_numero = Entry(frame_entrada)
        self.botao_adicionar = Button(frame_entrada, text="Adicionar", 
                                        command=self.adicionar_input_numero)
        

        tipos = ["Residencial", "Comercial", "Celular"]
        self.string_tipos = StringVar()
        self.string_tipos.set(tipos[0])
        self.menu_tipos = OptionMenu(frame_entrada, self.string_tipos, *tipos)
        
        self.menu_tipos.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.input_numero.pack(side="left", fill="both", expand=True, pady=5)
        self.botao_adicionar.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # ---criando a tabela
        frame_tabela = Frame(self)
        frame_tabela.pack_propagate(False)

        self.tabela = Treeview(frame_tabela)
        self.tabela["columns"] = ["id", "tipo", "numero"]
        self.tabela.heading("id", text="ID")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("numero", text="Número")
        self.tabela.column("#0", width=0, minwidth=0, stretch=False)
        self.tabela.column("id", width=50, minwidth=50, stretch=False)
        self.tabela.pack(fill="both", expand=True)

        # ---criando o botao de remover
        self.botao_remover = Button(self, text="Remover", 
                                    command=self.remover_numero_selecionado)
        
        # ---posicionando
        frame_entrada.pack(fill="x")
        frame_tabela.pack(fill="both", expand=True)
        self.botao_remover.pack(anchor="nw")

    def adicionar_input_numero(self, *args):
        """
        Adicionar ná tabela o número que está no campo de texto.
        Fica faltando implementar a validação.
        """
        # novos valores
        id_ = str(len(self.tabela.get_children())+1)
        tipo = self.string_tipos.get()
        numero = self.input_numero.get()
        # inserindo
        self.tabela.insert("", "end", values=(id_, tipo, numero))
        self.input_numero.delete(0, "end")
    
    def remover_numero_selecionado(self, *args):
        """
        Remover os números que estão selecionados na tabela e atualizar a coluna id.
        """
        selecoes = self.tabela.selection()
        if selecoes:
            # removendo os numeros selecionados
            self.tabela.delete(*selecoes)
            # guardando os restantes
            backup=[self.tabela.item(numero)["values"][1:] for numero in self.tabela.get_children()]
            # limpando completamente a tabela
            self.tabela.delete(*self.tabela.get_children())
            # inserindos os valores restantes com a coluna id atualizada
            for id_, dado in enumerate(backup, start=1):
                tipo = dado[0]
                numero = dado[1]
                self.tabela.insert("", "end", values=(id_, tipo, numero))
            
    
    def get_contato(self):
        """
        Retornar um dicionario com todos os contatos na tabela.
        """
        #print(self.tabela.get_children())
        contatos = {}
        for linha in self.tabela.get_children():
            valores = self.tabela.item(linha)["values"]
            contatos[valores[0]] = {"tipo":valores[1], "número":valores[2]}
        return contatos

    def set_contato(self, contatos):
        """
        param contatos: um dicionario.
        """
        for chave, valor in contatos.items():
            id_ = chave
            tipo = valor["tipo"]
            numero = valor["número"]
            self.tabela.insert("", "end", values=(id_, tipo, numero))


class SliderInput(Widget):
    """
    Um slider p/ definir algum valor númerico.
    """
    def __init__(self, *args, minimo=0, maximo=1500, **kwargs):
        super(SliderInput, self).__init__(*args, **kwargs)
        # ---criando os widgets
        # spinbox
        self.string_spinbox = StringVar()
        self.spinbox = Spinbox(self, from_=minimo, to=maximo, width=5, 
                                textvariable =self.string_spinbox) 
        # chamar o metodo atualizar_slider sempre que for digitado algo
        # no spinbox
        self.string_spinbox.trace("w", self.atualizar_slider)

        # filtrar para aceitar apenas numeros
        registro = get_tk(self).register(self.filtro_spinbox)
        self.spinbox.config(validate="key", validatecommand=(registro, "%P"))

        #slider
        self.slider = Scale(self, orient="horizontal", from_=minimo, to=maximo)
        self.slider["command"] = self.atualizar_spinbox

        # posicionando
        self.spinbox.pack(padx=5, pady=5, side="left", anchor="sw")
        self.slider.pack(padx=5, pady=5, side="left", fill="x", expand=True)
    
    def atualizar_spinbox(self, *args):
        # obtendo o valor do slider
        valor = self.slider.get()
        # atualizando o spinbox
        self.string_spinbox.set(str(valor))
    
    def atualizar_slider(self, *args):
        # obtendo o valor do spinbox
        valor = self.string_spinbox.get()
        # atualizando o valor para o tipo inteiro
        valor = int(valor) if valor.isnumeric() else valor
        # atualizando o slider
        if isinstance(valor, int):
            self.slider.set(valor)
    
    def filtro_spinbox(self, input):
        if input.isdigit():
            return True
        
        return False
        

    def get_valor(self):
        """
        Retornar o valor atual.
        """
        return self.slider.get()
    
    def set_valor(self, valor):
        """
        Definir o valor atual.
        """
        self.slider.set(valor)
        self.string_spinbox.set(str(valor))


class InseminacaoInput(Widget):
    def __init__(self, *args, **kwargs):
        super(InseminacaoInput, self).__init__(*args, **kwargs)
        # ---criando os widgets
        # radios buttons
        frame_radios = Frame(self)

        self.var_radio = IntVar()
        self.var_radio.set(False)

        self.radio_nao = Radiobutton(frame_radios, text="Não", value=False, 
                                                    variable=self.var_radio)
        

        self.radio_sim = Radiobutton(frame_radios, text="Sim", value=True, 
                                                    variable=self.var_radio)
                                            
        self.radio_nao["command"] = self.radiobutton_alterado
        self.radio_sim["command"] = self.radiobutton_alterado
        
        # data input 
        data_atual = datetime.now()
        data_atual_formatada=data_atual.strftime("%d%m%Y")
        self.data_input = MaskedWidget(self, "fixed", mask='99/99/9999')
        self.data_input.insert(0, data_atual_formatada)        
        
        # posicioanando
        self.radio_nao.pack(side="left", padx=5, pady=5)
        self.radio_sim.pack(side="right", padx=5, pady=5)        
        frame_radios.pack(fill="x", padx=5, pady=5)

    
    def radiobutton_alterado(self, *args):
        """
        Esconder ou mostrar o campo data.
        """
        if self.var_radio.get():
            self.data_input.pack()
        else:
            self.data_input.pack_forget()

    def get_inseminacao(self):
        """
        Retornar a data da inseminacao.
        """
        if self.var_radio.get():
            return self.data_input.get()
        else: 
            return None
    
    def set_inseminacao(self, data):
        """
        Definir a data.
        """
        if data is not None:
            self.var_radio.set(True)
            self.data_input.pack()
            self.data_input.insert(0, data.replace("/", "").replace("-", ""))
       

class OrdenhaInput(Widget):
    def __init__(self, *args, **kwargs):
        super(OrdenhaInput, self).__init__(*args, **kwargs)
        programa = get_tk(self)
        self.pack_propagate(False)
        self.dados_cadastrados = programa.get_dados()

        # ---criando o campo id
        self.input_id = Entry(self)
        registro = programa.register(self.filtro_input)
        self.input_id.config(validate="key", validatecommand=(registro, "%P"))

        # ---criando a tabela
        self.tabela = Treeview(self)
        self.tabela.column("#0", width=0, minwidth=0, stretch=False)

        # ----posicionando
        self.input_id.pack(padx=5, pady=5, fill="x")
        self.tabela.pack(padx=5, pady=5, fill="both", expand=True)

    def filtro_input(self, input):
        if input.isdigit():
            return True
        if input == "":
            return True
        return False     

    def get_input_id(self):
        """
        Retornar o valor que está no campo de texto.
        """
        return self.input_id.get()
    
    def set_input_id(self, input_id):
        self.input_id.delete(0, "end")
        self.input_id.insert(0, input_id)


class OrdenhaFuncionarioInput(OrdenhaInput):
    def __init__(self, *args, **kwargs):
        super(OrdenhaFuncionarioInput, self).__init__(*args, **kwargs)
       

        # configurando a tabela
        self.tabela.bind("<Double-Button-1>", self.preencher_input)
        self.tabela["columns"] = ["id", "nome"]
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.column("id", width=50, minwidth=50, stretch=False)
        

        funcionarios = self.dados_cadastrados["funcionários"]
        for _id, informacoes in funcionarios.items():
            self.tabela.insert("", "end", values=(_id, informacoes["nome"]))
    
    def preencher_input(self, *args):
        """
        Preencher o campo input com o valor da coluna id da linha selecionada.
        """
        selecoes = self.tabela.selection()
        if selecoes:
            selecao = selecoes[0]
            _id = self.tabela.item(selecao)["values"][0]
            self.set_input_id(_id)


class OrdenhaAnimalInput(OrdenhaInput):
    def __init__(self, *args, **kwargs):
        super(OrdenhaAnimalInput, self).__init__(*args, **kwargs)
       
        # configurando a tabela
        self.tabela.bind("<Double-Button-1>", self.preencher_input)
        self.tabela["columns"] = ["id"]
        self.tabela.heading("id", text="ID")
        
        animais = self.dados_cadastrados["animais"]
        for _id in animais.keys():
            self.tabela.insert("", "end", values=(_id,))
    
    def preencher_input(self, *args):
        """
        Preencher o campo input com o valor da coluna id da linha selecionada.
        """
        selecoes = self.tabela.selection()
        if selecoes:
            selecao = selecoes[0]
            _id = self.tabela.item(selecao)["values"][0]
            self.set_input_id(_id)
    