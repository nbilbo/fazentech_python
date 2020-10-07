# coding: utf-8

from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import (QTableView, QGroupBox, QGridLayout, QLineEdit, QComboBox, QPushButton)



# ---modelo para usar na tabela
class Modelo(QAbstractTableModel):
    def __init__(self):
        super(Modelo, self).__init__()
        self.dados = []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            valor = self.dados[index.row()][index.column()]
            return str(valor)
    
    def rowCount(self, index):
        return len(self.dados)
    
    def columnCount(self, index):
        return len(self.dados[0]) if self.dados else 0
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['tipo', 'número'][section]
            if orientation == Qt.Vertical:
                return section


# ---um QGroupBox com uma tabela
class Contato(QGroupBox):
    def __init__(self):
        super(Contato, self).__init__()
        self.setTitle('Contato')

        # ---tabela
        # instanciando o modelo 
        self.modelo = Modelo()
        # isntanciando a tabela
        self.tabela = QTableView()
        self.tabela.setModel(self.modelo)
        # expando a ultima coluna
        self.tabela.horizontalHeader().setStretchLastSection(True)
        # redimensionando a largura da primeira coluna
        self.tabela.resizeColumnToContents(0)

        # ---campo para adicionar um novo numero
        # combobox
        self.combobox = QComboBox()
        self.combobox.addItem('Residencial')
        self.combobox.addItem('Comercial')
        self.combobox.addItem('Celular')
        # input
        self.input_numero = QLineEdit()
        # botao adicionar
        self.botao_add = QPushButton(text='Adicionar')
        self.botao_add.pressed.connect(self.adicionar)

        # ---botao para remover um numero selecionado
        self.botao_remove = QPushButton(text='Remover')
        self.botao_remove.pressed.connect(self.remover)

        # ---grid layout que vai organizar todos os widgets
        layout = QGridLayout()
        # campo do novo numero
        layout.addWidget(self.combobox, 0, 0)
        layout.addWidget(self.input_numero, 0, 1)
        layout.addWidget(self.botao_add, 0, 2)
        # tabela
        layout.addWidget(self.tabela, 1, 0, 1, 3)
        # botao remove
        layout.addWidget(self.botao_remove, 4, 0)

        #setLayout
        self.setLayout(layout)
    
    def adicionar(self):
        '''
        Obter as informações dos campos de entrada de dados e adicioanar na tabela.
        '''
        tipo = self.combobox.currentText()
        numero = self.input_numero.text()

        # validação
        if tipo and numero:
            self.modelo.dados.append([tipo, numero])
            self.modelo.layoutChanged.emit()
            self.tabela.resizeColumnToContents(0)
            self.input_numero.setText('')

    def remover(self):
        '''
        Remover a linha que está selecionada.
        '''
        indexes = self.tabela.selectedIndexes()
        
        if indexes:
            row = indexes[0].row()
            del self.modelo.dados[row]
            self.modelo.layoutChanged.emit()
            self.tabela.resizeColumnToContents(0)
            self.tabela.clearSelection()
    
    def get_contato(self):
        return self.modelo.dados


# over view
if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication, QMainWindow


    app = QApplication([])
    app.setFont(QFont('Georgia', 14))

    programa = QMainWindow()
    programa.setCentralWidget(Contato())
    programa.centralWidget().modelo.dados.append(['Celular', '(011) 91234-5678'])
    programa.centralWidget().modelo.layoutChanged.emit()
    programa.show()

    sys.exit(app.exec_())
