# coding: utf-8

from os import path
from json import load
from PyQt5.QtWidgets import QGroupBox, QFormLayout, QComboBox, QLineEdit, QTextEdit, QLabel


# ---carregar os estados e cidades
CURRENT_DIR = path.dirname(path.abspath(__file__))
#ESTADOS_JSON = path.join(CURRENT_DIR, 'cidades-estados-brasil-json', 'Estados.json')
#CIDADES_JSON = path.join(CURRENT_DIR, 'cidades-estados-brasil-json', 'Cidades.json')


with open(path.join(CURRENT_DIR, 'cidades-estados-brasil-json', 'Estados.json'), 'r', encoding='utf-8') as f:
    ESTADOS_JSON = load(f)

with open(path.join(CURRENT_DIR, 'cidades-estados-brasil-json', 'Cidades.json'), 'r', encoding='utf-8') as f:
    CIDADES_JSON = load(f)


class Endereco(QGroupBox):
    def __init__(self):
        super(Endereco, self).__init__()
        self.setTitle('Endereço')
        # ---inputs
        self.input_rua = QLineEdit()
        self.input_bairro = QLineEdit()
        self.input_numero = QLineEdit()
        self.input_completo = QTextEdit()

        # ---combobox estado (estado inicial)
        self.estado_sigla = 'AC'
        self.combobox_estado = QComboBox()
        self.combobox_estado.addItems([estado['Nome'] for estado in ESTADOS_JSON])
        self.combobox_estado.currentIndexChanged.connect(self.atualizar_combobox_cidade)

        # ---combobox cidade (cidadades iniciais)
        self.combobox_cidade = QComboBox()
        self.combobox_cidade.addItems([cidade['Nome'] for cidade in CIDADES_JSON if cidade['Estado']=='1'])

        # ---layout
        layout = QFormLayout()
        layout.addRow(QLabel('Número'), self.input_numero)
        layout.addRow(QLabel('Rua'), self.input_rua)
        layout.addRow(QLabel('Bairro'), self.input_bairro)
        layout.addRow(QLabel('Cidade'), self.combobox_cidade)
        layout.addRow(QLabel('Estado'), self.combobox_estado)
        layout.addRow(QLabel('Complemento'), self.input_completo)
        
        self.setLayout(layout)
    
    def atualizar_combobox_cidade(self):
        # limpando todo o combobox
        self.combobox_cidade.clear()
        # obtendo o nome do estado
        estado_nome = self.combobox_estado.currentText()
        id_estado = 0
        # percorrendo por todos os estado p/ obter o id atual.
        for estado in ESTADOS_JSON:
            if estado['Nome'] == estado_nome:
                id_estado, self.estado_sigla = estado['ID'], estado['Sigla']
                break
        # atualizando o combobox
        if id_estado:
            self.combobox_cidade.addItems([cidade['Nome'] for cidade in CIDADES_JSON if cidade['Estado']==str(id_estado)])

    def get_endereco(self):
        '''
        Retornar um dicionario com os valores dos campos.
        '''
        endereco = {}
        endereco['rua'] = self.input_rua.text()
        endereco['bairro'] = self.input_bairro.text()
        endereco['numero'] = self.input_numero.text()
        endereco['cidade'] = self.combobox_cidade.currentText()
        endereco['estado'] = self.combobox_estado.currentText()
        endereco['sigla'] = self.estado_sigla
        endereco['complemento'] = self.input_completo.toPlainText()
        return endereco

if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication
    from window import Window


    app = QApplication([])
    app.setFont(QFont('Georgia', 14))

    window = Window()
    window.setCentralWidget(Endereco())
    window.show()
    print(window.centralWidget().get_endereco())

    sys.exit(app.exec_())
