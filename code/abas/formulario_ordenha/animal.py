from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import (QGroupBox, QFormLayout, QGridLayout, 
                                QLineEdit, QTableView)


class GroupId(QGroupBox):
    def __init__(self):
        super(GroupId, self).__init__()
        self.setTitle('Id')
        self.input = QLineEdit()

        layout = QFormLayout()
        layout.addWidget(self.input)
        self.setLayout(layout)
    
    def get_input(self):
        return self.input.text()
    
    def set_input(self, value):
        self.input.setText(value)


class Model(QAbstractTableModel):
    def __init__(self, *args, data=None, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.backup = self._data = data or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()]
            return str(value)

    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return 1
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return 'Id'
    

class Animal(QGroupBox):
    def __init__(self):
        super(Animal, self).__init__()
        self.setTitle('Animal')
        # group id
        self.group_id = GroupId()
        self.group_id.input.textChanged.connect(self.filter_by_id)

        # table
        self.model = Model()
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.doubleClicked.connect(self.set_fields)

        # form
        form = QFormLayout()
        form.addWidget(self.group_id)

        # main layout
        layout = QGridLayout()
        layout.addLayout(form, 0, 0)
        layout.addWidget(self.table, 0, 1)
        self.setLayout(layout)
    
    def filter_by_id(self):
        '''
        Filtrar pelo id.
        '''
        id_value = self.group_id.get_input().strip()

        if id_value:
            data = [id_ for id_ in self.model.backup if str(id_).startswith(id_value)]
            self.model._data = data
        else:
            self.model._data = self.model.backup
        
        self.model.layoutChanged.emit()

    def get_animal(self):
        '''
        Retornar um dicionario com os valores dos campos.
        '''
        resultado = {}
        resultado['id'] = self.group_id.get_input()
        return resultado

    def set_fields(self):
        '''
        Preencher o campo id sempre que for clicado 2x em uma linha da tabela.
        '''
        indexes = self.table.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            self.group_id.set_input(str(self.model._data[row]))

    def set_data(self, value=None):
        '''
        Definir os atributos backup e _data.
        '''
        self.model.backup = self.model._data = value or []
        self.model.layoutChanged.emit()




if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication, QMainWindow


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))
    
    programa = QMainWindow()
    programa.setCentralWidget(Animal())
    programa.centralWidget().set_data([1, 2, 3, 22, 31, 55])
    programa.setWindowTitle('Testes')
    programa.resize(900, 500)
    programa.show()

    sys.exit(app.exec_())


