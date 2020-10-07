# coding: utf-8


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QGroupBox, QSpinBox, QSlider, QFormLayout)


class MySlider(QGroupBox):
    title = 'my slider'
    def __init__(self, *args, **kwargs):
        super(MySlider, self).__init__(*args, **kwargs)
        self.setTitle(self.title)
        self.spinbox = QSpinBox()
        self.slider = QSlider(orientation=Qt.Horizontal)

        layout = QFormLayout()
        layout.addRow(self.spinbox, self.slider)
        self.setLayout(layout)


class Inteiro(MySlider):
    title = 'Inteiro'


class Decimal(MySlider):
    title = 'Decimal'


class Litros(QGroupBox):
    def __init__(self):
        super(Litros, self).__init__()
        self.setTitle('Litros')
        self.spinbox = QSpinBox()
        self.slider = QSlider(orientation=Qt.Horizontal)

        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinbox.setValue)

        layout = QFormLayout()
        layout.addRow(self.spinbox, self.slider)
        self.setLayout(layout)
    
    def get_litros(self):
        return self.spinbox.value()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(Litros())
    programa.resize(900, 500)
    programa.setWindowTitle('Testes')
    programa.show()

    sys.exit(app.exec_())


