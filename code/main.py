# coding: utf-8


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from abas import (Funcionarios, Animais, Ordenhas)


class Program(QMainWindow):
    def __init__(self):
        super(Program, self).__init__()
        self.settings()
        self.setCentralWidget(self.create_central_widget())
    
    def settings(self):
        self.setWindowTitle('Fazentech Demo')
        self.resize(1100, 600)
        self.setFont(QFont('Georgia', 12))

    def create_central_widget(self):
        self.functionarys = Funcionarios()
        self.animals = Animais()
        self.milking = Ordenhas()

        central_widget = QTabWidget()
        central_widget.addTab(self.functionarys, 'Funcionários')
        central_widget.addTab(self.animals, 'Animais')
        central_widget.addTab(self.milking, 'Ordenhas')

        return central_widget


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication


    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec_())
