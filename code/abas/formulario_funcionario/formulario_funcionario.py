# coding: utf-8


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
                            QGroupBox, QFormLayout,  QScrollArea, 
                            QVBoxLayout, QPushButton)
from .genero import Genero
from .nome import Nome
from .cpf import Cpf
from .endereco import Endereco
from .contato import Contato


class FormularioFuncionario(QWidget):
    def __init__(self, *args, **kwargs):
        super(FormularioFuncionario, self).__init__(*args, **kwargs)
        self.setWindowTitle('Formulário funcionário')
        self.resize(900, 600)
        self.setFont(QFont('Georgia', 12))
        
        # grupos
        self.grupo_nome = Nome()
        self.grupo_genero = Genero()
        self.grupo_cpf = Cpf()
        self.endereco = Endereco()
        self.contato = Contato()
        self.contato.setFixedHeight(400)
        self.botao_confirmar = QPushButton('Confirmar')
       
        # layout
        layout = QFormLayout()
        layout.addWidget(self.grupo_nome)
        layout.addWidget(self.grupo_genero)
        layout.addWidget(self.grupo_cpf)
        layout.addWidget(self.endereco)
        layout.addWidget(self.contato)
        layout.addWidget(self.botao_confirmar)
        
        # scroll area
        # como possui muitas informações, é necessesário um scroll para navegar
        widget_scroll = QWidget()
        widget_scroll.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget_scroll)

        layout_scroll = QVBoxLayout()
        layout_scroll.addWidget(scroll_area)
        self.setLayout(layout_scroll)

    def get_formulario_funcionario(self):
        resultado = {}

        resultado['nome'] = self.grupo_nome.get_nome()
        resultado['genero'] = self.grupo_genero.get_genero()
        resultado['cpf'] = self.grupo_cpf.get_cpf()
        resultado['endereco'] = self.endereco.get_endereco()
        resultado['contato'] = self.contato.get_contato()
        
        return resultado

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFont
    from window import Window

    app = QApplication([])
    app.setFont(QFont('Geogia', 12))

    programa = Window()
    programa.setCentralWidget(FormularioFuncionario())
    programa.show()
    print(programa.centralWidget().get_formulario_funcionario())
    sys.exit(app.exec_())
