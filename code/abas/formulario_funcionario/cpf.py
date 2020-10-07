from PyQt5.QtWidgets import QGroupBox, QFormLayout, QLineEdit


class Cpf(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Cpf, self).__init__(*args, **kwargs)
        self.setTitle('Cpf')
        self.input_cpf = QLineEdit()

        layout = QFormLayout()
        layout.addWidget(self.input_cpf)
        self.setLayout(layout)
    
    def get_cpf(self):
        return self.input_cpf.text()


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication
    from window import Window


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = Window()
    programa.setCentralWidget(Cpf())
    programa.show()

    sys.exit(app.exec_())

