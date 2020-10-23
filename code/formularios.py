# coding: utf-8

"""
Não tente entender esses códigos, confesso que ficou confuso.
"""
from tkinter import (Frame, Button, Toplevel)
from widgets import (NormalInput, GeneroInput, EnderecoInput,
                     ContatoInput, SliderInput, InseminacaoInput,
                     OrdenhaFuncionarioInput, OrdenhaAnimalInput)
from utils import get_tk

####
# Formulários
####

# ---formulario
class Formulario(Toplevel):
    titulo_janela = "Formulário"

    def __init__(self, parent, id=None):
        super(Formulario, self).__init__()
        self.set_parent(parent)
        self.set_id(id)
        self.configuracoes()
    
    def configuracoes(self):
        self.title(self.titulo_janela)
        self.geometry("400x550+0+0")
        
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_id(self):
        return self._id
    
    def set_id(self, _id):
        self._id = _id


# ---formulario funcionario
class FormularioFuncionario(Formulario):
    titulo_janela = "Formulário novo funcionário"

    def __init__(self, *args, **kwargs):
        super(FormularioFuncionario, self).__init__(*args, **kwargs)

        # criando o campo nome
        self.nome_input = NormalInput(self, label="Nome")

        # criando o campo gênero
        self.genero_input = GeneroInput(self, label="Gênero")

        # criando o campo endereço
        self.endereco_input = EnderecoInput(self, label="Endereço")

        # criando o campo contatos
        self.contato_input = ContatoInput(self, label="Contato")

        # criando o botão de confirmação
        self.botao_confirmacao = Button(self, text="Confirmar", borderwidth=5, relief="raised")
        self.botao_confirmacao["command"] = self.cadastrar

        # posicioanando 
        self.nome_input.pack(padx=5, pady=10, fill="x")
        self.genero_input.pack(padx=5, pady=10, fill="x")
        self.endereco_input.pack(padx=5, pady=10, fill="x")
        self.contato_input.pack(padx=5, pady=0, fill="both", expand=True)
        self.botao_confirmacao.pack(padx=5, pady=5)
    
    def cadastrar(self):
        """
        Cadastrar os dados.
        """
        informacoes = self.get_dados()
        programa = get_tk(self)
        programa.cadastrar(informacoes=informacoes, tabela="funcionários")
        self.destroy()
    
    def atualizar(self):
        """
        Atualizar os dados. 
        """
        informacoes = self.get_dados()
        programa = get_tk(self) 
        programa.atualizar(self.get_id(), informacoes, "funcionários")
        self.destroy()

    def get_dados(self):
        """
        Retornar um dicionario com os valores dos campos.
        """
        dados = {}
        dados["nome"] = self.nome_input.get_input()
        dados["gênero"] = self.genero_input.get_genero()
        dados["endereço"] = self.endereco_input.get_endereco()
        dados["contato"] = self.contato_input.get_contato()
        return dados
    
    def set_dados(self, dados):
        """
        Preencher os campos com os dados.
        """
        self.nome_input.set_input(dados["nome"])
        self.genero_input.set_genero(dados["gênero"])
        self.endereco_input.set_estado(dados["endereço"]["estado"])
        self.endereco_input.set_cidade(dados["endereço"]["cidade"])
        self.contato_input.set_contato(dados["contato"])


class FormularioAtulizarFuncionario(FormularioFuncionario):
    titulo_janela = "Atualizar funcionário"

    def __init__(self, *args, **kwargs):
        super(FormularioAtulizarFuncionario, self).__init__(*args, **kwargs)
        # ---recuperando todas as informacoes desse funcionario
        informacao_funcionario = get_tk(self).get_dados()["funcionários"][self.get_id()]
        # ---preenchendo os campos
        self.set_dados(informacao_funcionario)
        # ---definindo qual funcao o botao deve chamar
        self.botao_confirmacao["command"] = self.atualizar


# ---formulario animal
class FormularioAnimal(Formulario):
    titulo_janela = "Formulário novo animal"

    def __init__(self, *args, **kwargs):
        super(FormularioAnimal, self).__init__(*args, **kwargs)

        # ---criando o campo raça
        self.raca_input = NormalInput(self, "Raça")

        # ---criando o campo peso
        self.peso_input = SliderInput(self, "Peso (Kg)")

        # ---criando o campo de ruminação
        self.ruminacao_input = SliderInput(self, "Ruminação (minutos)", maximo=150)

        # ---criando o campo de inseminação
        self.inseminacao_input = InseminacaoInput(self, "Inseminação")

        # ---criando o botao
        self.botao_confirmacao = Button(self, text="Confirmar", 
                                        borderwidth=5, relief="raised", command=self.cadastrar)

        # ---posicionando
        self.raca_input.pack(padx=5, pady=10, fill="x")
        self.peso_input.pack(padx=5, pady=10, fill="x")
        self.ruminacao_input.pack(padx=5, pady=10, fill="x")
        self.inseminacao_input.pack(padx=5, pady=10, fill="both")
        self.botao_confirmacao.pack(padx=5, pady=5, anchor="s", expand=True)

        # ---debug
        #print(get_tk(self).get_dados()["animais"]["1"]["inseminação"])

    def cadastrar(self):
        """
        Inserir as novas informacoes no arquivo json.
        """
        informacoes = self.get_dados()
        
        programa = get_tk(self)
        programa.cadastrar(informacoes=informacoes, tabela="animais")
        self.destroy()
    
    def atualizar(self):
        """
        Atualizar o arquivo json com as novas informações.
        """
        informacoes = self.get_dados()
        programa = get_tk(self) 
        programa.atualizar(id=self.get_id(), informacoes=informacoes,
                                                     tabela="animais")
        self.destroy()    

    def get_dados(self):
        informacoes = {}
        informacoes["raça"] = self.raca_input.get_input()
        informacoes["peso"] = self.peso_input.get_valor()
        informacoes["ruminação"] = self.ruminacao_input.get_valor()
        informacoes["inseminação"] = self.inseminacao_input.get_inseminacao()
        return informacoes    

    def set_dados(self, dados):
        """
        Preencher os campos com os dados.
        """
        self.raca_input.set_input(dados["raça"])
        self.peso_input.set_valor(dados["peso"])
        self.ruminacao_input.set_valor(dados["ruminação"])
        self.inseminacao_input.set_inseminacao(dados["inseminação"])
     

class FormularioAtualizarAnimal(FormularioAnimal):
    titulo_janela = "Atualizar animal"

    def __init__(self, *args, **kwargs):
        super(FormularioAtualizarAnimal, self).__init__(*args, **kwargs)
        informacao_animal = get_tk(self).get_dados()["animais"][self.get_id()]
        self.set_dados(informacao_animal)
        self.botao_confirmacao["command"] = self.atualizar


# ---formulario ordenha
class FormularioOrdenha(Formulario):
    titulo_janela = "Formulário ordenha"
    def __init__(self, *args, **kwargs):
        super(FormularioOrdenha, self).__init__(*args, **kwargs)
        # ---criando o campo ususario
        self.funcionario_input = OrdenhaFuncionarioInput(parent=self, label="Funcionário")

        # ---criando o campo animal
        self.animal_input = OrdenhaAnimalInput(parent=self, label="Animal")

        # ---criando o campo litro
        self.litros_input = SliderInput(parent=self, label="Litros", maximo=150)

        # ---criando o botao
        self.botao_confirmacao = Button(self, text="Confirmar", borderwidth=5, relief="raised", 
                                        command=self.cadastrar)

        # ---posicionandando
        self.funcionario_input.pack(padx=5, pady=5, fill="both", expand=True)
        self.animal_input.pack(padx=5, pady=5, fill="both", expand=True)
        self.litros_input.pack(padx=5, pady=5, fill="x")
        self.botao_confirmacao.pack(padx=5, pady=5)

    def cadastrar(self):
        """
        Cadastrar as informações.
        """
        informacoes = self.get_dados()
        programa = get_tk(self)
        programa.cadastrar(informacoes=informacoes, tabela="ordenhas")
        self.destroy()
    
    def atualizar(self):
        """
        Atualizar as informações.
        """
        informacoes = self.get_dados()
        programa = get_tk(self) 
        programa.atualizar(id=self.get_id(), informacoes=informacoes,
                                                     tabela="ordenhas")
        self.destroy()

    def get_dados(self):
        """
        Retornar os dados do formulario.
        """
        dados = {}
        dados["funcionário"] = self.funcionario_input.get_input_id()
        dados["animal"] = self.animal_input.get_input_id()
        dados["litros"] = self.litros_input.get_valor()
        return dados
    
    def set_dados(self, dados):
        """
        Definir os dados do formulario.
        """
        self.funcionario_input.set_input_id(dados["funcionário"])
        self.animal_input.set_input_id(dados["animal"])
        self.litros_input.set_valor(dados["litros"])


class FormularioAtualizarOrdenha(FormularioOrdenha):
    def __init__(self, *args, **kwargs):
        super(FormularioAtualizarOrdenha, self).__init__(*args, **kwargs)
        
        # ---preenchendo os campos
        informacao_ordenha  = get_tk(self).get_dados()["ordenhas"][self.get_id()]
        self.set_dados(informacao_ordenha)

        # ---atualizando o botao
        self.botao_confirmacao["command"] = self.atualizar
        