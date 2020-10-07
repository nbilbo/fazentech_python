# coding: utf-8


from PyQt5.QtWidgets import QGroupBox, QLineEdit, QFormLayout


class Especie(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Especie, self).__init__(*args, **kwargs)
        self.setTitle('Especie')
        self.input_especie = QLineEdit()

        layout = QFormLayout()
        layout.addWidget(self.input_especie)
        self.setLayout(layout)
    
    def get_especie(self):
        return self.input_especie.text()
        

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = QMainWindow()
    programa.setCentralWidget(Especie())
    programa.resize(900, 500)
    programa.show()

    sys.exit(app.exec_())
