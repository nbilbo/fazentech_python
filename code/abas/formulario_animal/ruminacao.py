from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGroupBox, QSlider, QSpinBox, 
                            QLabel, QFormLayout)


class Ruminacao(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Ruminacao, self).__init__(*args, **kwargs)
        self.setTitle('Ruminação(minutos)')

        self.spinbox = QSpinBox(minimum=0)
        self.slider = QSlider(orientation=Qt.Horizontal, minimum=0)

        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinbox.setValue)

        layout = QFormLayout()
        layout.addRow(self.spinbox, self.slider)
        self.setLayout(layout)
    
    def get_ruminacao(self):
        return self.spinbox.value()


if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication, QMainWindow


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.resize(900, 500)
    programa.setCentralWidget(Ruminacao())
    programa.show()
    
    sys.exit(app.exec_())
