from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGroupBox, QFormLayout, QSpinBox, 
                            QSlider)


class Peso(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Peso, self).__init__(*args, **kwargs)
        self.setTitle('Peso(Kg)')

        self.spinbox = QSpinBox(minimum=0, maximum=1500)
        self.slider = QSlider(orientation=Qt.Horizontal, minimum=0, maximum=1500)
        
        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinbox.setValue)

        layout = QFormLayout()
        layout.addRow(self.spinbox, self.slider)
        self.setLayout(layout)
    
    def get_peso(self):
        return self.spinbox.value()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.resize(900, 500)
    programa.setCentralWidget(Peso())
    programa.show()
    
    sys.exit(app.exec_())
