from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QLineEdit, QFormLayout


class Nome(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Nome, self).__init__(*args, **kwargs)
        self.setTitle('Nome')
        self.input_nome = QLineEdit()

        layout = QFormLayout()
        layout.addWidget(self.input_nome)
        self.setLayout(layout)
    
    def get_nome(self):
        return self.input_nome.text()


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication
    from window import Window


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    programa = Window()
    programa.setCentralWidget(Nome())
    programa.show()

    sys.exit(app.exec_())

