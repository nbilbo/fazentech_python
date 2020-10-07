# coding: utf-8


from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import (QWidget, QTableView, QPushButton, 
                            QGridLayout, QLineEdit)


class TabelaDefault(QWidget):
    model = None
    formulario_adicionar = None

    def __init__(self):
        super(TabelaDefault, self).__init__()
        self.formularios = list()

        # table
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)

        # buttons
        self.button_add = QPushButton('Adicionar')
        self.button_update = QPushButton('Atualizar')
        self.butotn_remove = QPushButton('Remover')

        self.button_add.pressed.connect(self.abrir_formulario_adicionar)
        self.button_update.pressed.connect(self.abrir_formulario_atualizar)
        self.butotn_remove.pressed.connect(self.abrir_formulario_remover)

        # input
        self.input = QLineEdit()

        # layout
        layout = QGridLayout()
        layout.addWidget(self.input, 0, 0, 1, 3)
        layout.addWidget(self.table, 1, 0, 1, 3)
        layout.addWidget(self.button_add, 2, 0)
        layout.addWidget(self.button_update, 2, 1)
        layout.addWidget(self.butotn_remove, 2, 2)
        self.setLayout(layout)
    
    def abrir_formulario_adicionar(self):
        if self.formulario_adicionar:
            novo_form = self.formulario_adicionar()
            self.formularios.append(novo_form)
            novo_form.show()
          

    def abrir_formulario_atualizar(self):
        pass

    def abrir_formulario_remover(self):
        pass


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    window = QMainWindow()
    window.setCentralWidget(TabelaDefault())
    window.resize(900, 500)
    window.show()

    sys.exit(app.exec_())
