# coding: utf-8


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from .especie import Especie
from .peso import Peso
from .ruminacao import Ruminacao
from .inseminacao import Inseminacao


class FormularioAnimal(QWidget):
    def __init__(self):
        super(FormularioAnimal, self).__init__()
        self.setWindowTitle('Formulário animal')
        self.resize(900, 600)
        self.setFont(QFont('Georgia', 12))

        self.especie = Especie()
        self.peso = Peso()
        self.ruminacao = Ruminacao()
        self.inseminacao = Inseminacao()
        self.botao_confirmar = QPushButton('Confirmar')

        layout = QVBoxLayout()
        layout.addWidget(self.especie)
        layout.addWidget(self.peso)
        layout.addWidget(self.ruminacao)
        layout.addWidget(self.inseminacao)
        layout.addWidget(self.botao_confirmar)
        self.setLayout(layout)
    
    def get_formulario_animal(self):
        resultado = {}
        resultado['especie'] = self.especie.get_especie()
        resultado['peso'] = self.peso.get_peso()
        resultado['ruminacao'] = self.ruminacao.get_ruminacao()
        resultado['inseminacao'] = self.inseminacao.get_inseminacao()
        return resultado


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(FormularioAnimal())
    programa.resize(900, 500)
    programa.setWindowTitle('PyQt5 Window')
    programa.show()
    print(programa.centralWidget().get_formulario_animal())
    
    sys.exit(app.exec_())
