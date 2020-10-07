# coding: utf-8


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QFormLayout, QSlider, QSpinBox


class Temperatura(QGroupBox):
    def __init__(self):
        super(Temperatura, self).__init__()
        self.setTitle('Temperatura')
        self.spinbox = QSpinBox()
        self.slider = QSlider(orientation=Qt.Horizontal)

        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinbox.setValue)

        layout = QFormLayout()
        layout.addRow(self.spinbox, self.slider)
        self.setLayout(layout)
    
    def get_temperatura(self):
        return self.spinbox.value()


if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication, QMainWindow


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(Temperatura())
    programa.resize(900, 500)
    programa.setWindowTitle('Testes')
    programa.show()

    sys.exit(app.exec_())
