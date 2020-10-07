# coding: utf-8


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QFormLayout, QScrollArea, 
                            QPushButton)
from .funcionario import Funcinario
from .animal import Animal
from .litros import Litros
from .temperatura import Temperatura
from .ocorrencia import Ocorrencia


class FormularioOrdenha(QWidget):
    def __init__(self):
        super(FormularioOrdenha, self).__init__()
        self.setWindowTitle('Formulário ordenha')
        self.resize(900, 600)
        self.setFont(QFont('Georgia', 12))

        self.funcionario = Funcinario()
        self.animal = Animal()
        self.litros = Litros()
        self.temperatura = Temperatura()
        self.ocorrencia = Ocorrencia()
        self.botao_confirmar = QPushButton('Confirmar')

        self.funcionario.setFixedHeight(400)
        self.animal.setFixedHeight(400)

        # layout 
        layout = QFormLayout()
        layout.setVerticalSpacing(50)
        layout.addWidget(self.funcionario)
        layout.addWidget(self.animal)
        layout.addWidget(self.litros)
        layout.addWidget(self.temperatura)
        layout.addWidget(self.ocorrencia)
        layout.addWidget(self.botao_confirmar)

        # scroll area
        widget_scroll = QWidget()
        widget_scroll.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidget(widget_scroll)
        scroll_area.setWidgetResizable(True)

        # mainlayout 
        main_layout = QFormLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
    
    def get_formulario_ordenha(self):
        resultado = {}

        resultado['funcionario'] = self.funcionario.get_funcionario()
        resultado['animal'] = self.animal.get_animal()
        resultado['litros'] = self.litros.get_litros()
        resultado['temperatura'] = self.temperatura.get_temperatura()
        resultado['ocorrencia'] = self.ocorrencia.get_ocorrencia()

        return resultado


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(FormularioOrdenha())
    programa.resize(1100, 600)
    programa.setWindowTitle('Testes formulario')
    programa.show()

    form = programa.centralWidget()
    form.funcionario.set_data([
        [1, 'Andreza'], [11, 'Carlos Bras'], [111, 'Antonio']
    ])
    form.animal.set_data([3, 33, 333])
    print(form.get_formulario_ordenha())

    sys.exit(app.exec_())
