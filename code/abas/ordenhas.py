# coding: utf-8


from PyQt5.QtCore import Qt, QAbstractTableModel
from .tabela_default import TabelaDefault
from .formulario_ordenha import FormularioOrdenha


class Model(QAbstractTableModel):
    def __init__(self, data=None):
        super(Model, self).__init__()
        self.backup = self._data = data or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            return str(value)
    
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return 3

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['Id', 'Ocorrencia', 'Funcionario'][section]


class Ordenhas(TabelaDefault):
    model = Model()
    formulario_adicionar = FormularioOrdenha


if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication, QMainWindow


    app = QApplication([])
    app.setFont(QFont('Geogia', 12))
    window = QMainWindow()
    window.setCentralWidget(Ordenhas())
    window.resize(900, 600)
    window.show()

    sys.exit(app.exec_())







