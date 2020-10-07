# coding: utf-8


from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QGroupBox, QFormLayout, QDateTimeEdit


class Ocorrencia(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Ocorrencia, self).__init__(*args, **kwargs)
        self.setTitle('Ocorrência')
        
        self.input_ocorrencia = QDateTimeEdit()
        self.input_ocorrencia.setDateTime(QDateTime.currentDateTime())
        self.input_ocorrencia.setDisplayFormat('dd/MM/yyyy HH:mm')

        layout = QFormLayout()
        layout.addWidget(self.input_ocorrencia)
        self.setLayout(layout)
    
    def get_ocorrencia(self):
        '''
        Retornar um dicionario com o valor da data e hora.
        '''
        resultado = {}
        resultado['date_eua'] = self.input_ocorrencia.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        resultado['date_br'] = self.input_ocorrencia.dateTime().toString('dd-MM-yyyy HH:mm:ss')
        return resultado


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Geogia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(Ocorrencia())
    programa.resize(900, 500)
    programa.setWindowTitle('Testes')
    programa.show()
    # método get_ocorrencia
    print(programa.centralWidget().get_ocorrencia())

    sys.exit(app.exec_())
