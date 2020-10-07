from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import (QGroupBox, QGridLayout, QFormLayout, 
                            QLabel, QLineEdit, QTableView)


class Group(QGroupBox):
    title = 'Group'
    def __init__(self):
        super(Group, self).__init__()
        self.setTitle(self.title)
        self.input = QLineEdit()

        layout = QFormLayout()
        layout.addWidget(self.input)
        self.setLayout(layout)
    
    def get_input(self):
        return self.input.text()
    
    def set_input(self, value):
        self.input.setText(value)


class GroupId(Group):
    title = 'Id'


class GroupName(Group):
    title = 'Nome'


class Model(QAbstractTableModel):
    def __init__(self, *args, data=None, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.backup = self._data = data or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            return str(value)
    
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return 2
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['Id', 'Nome'][section]
    

class Funcinario(QGroupBox):
    def __init__(self):
        super(Funcinario, self).__init__()
        self.setTitle('Funcionário')

        # group id
        self.group_id = GroupId()
        self.group_id.input.textChanged.connect(self.filter_by_id)

        # group name
        self.group_name = GroupName()
        self.group_name.input.textChanged.connect(self.filter_by_name)

        # table
        self.table_model = Model()
        self.table = QTableView()
        self.table.setModel(self.table_model)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.doubleClicked.connect(self.set_fields)
        
        # formlayout
        form = QFormLayout()
        form.addWidget(self.group_id)
        form.addWidget(self.group_name)

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
            data = [row for row in self.table_model.backup if str(row[0]).startswith(id_value)]
        else:
            data = self.table_model.backup

        self.table_model._data = data
        self.table_model.layoutChanged.emit()
        
    
    def filter_by_name(self):
        '''
        Filtrar pelo nome.
        '''
        name_value = self.group_name.get_input().strip()

        if name_value:
            data = [row for row in self.table_model.backup if str(row[1]).startswith(name_value)]
        else:
            data = self.table_model.backup
        
        self.table_model._data = data
        self.table_model.layoutChanged.emit()
    
    def set_fields(self):
        '''
        Preencher os campos de id e nome sempre que clicar 2x em uma linha da tabela.
        '''
        indexes = self.table.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            id_value, name_value = self.table_model._data[row]
            self.group_id.set_input(str(id_value))
            self.group_name.set_input(str(name_value))
    
    def get_funcionario(self):
        '''
        Retornar um dicionario com os valores dos campos.
        '''
        resultado = {}
        resultado['id'] = self.group_id.get_input().strip()
        resultado['name'] = self.group_name.get_input().strip()
        return resultado
    
    def set_data(self, data=None):
        '''
        Definir os atributos backup e _data.
        '''
        self.table_model.backup = self.table_model._data = data or []
        self.table_model.layoutChanged.emit()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(Funcinario())
    programa.centralWidget().set_data([
        [1, 'Carlos'],
        [11, 'Gabriel']
    ])
    programa.setWindowTitle('Testes')
    programa.resize(900, 500)
    programa.show()

    sys.exit(app.exec_())



