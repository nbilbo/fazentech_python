# coding: utf-8

from PyQt5.QtWidgets import QGroupBox, QRadioButton, QFormLayout


class Genero(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Genero, self).__init__(*args, **kwargs)
        self.setTitle('Gênero')
        #self.setMaximumHeight(70)

        # radio buttons
        self.radio_femi = QRadioButton('Femi')
        self.radio_masc = QRadioButton('Masc')
        self.radio_masc.setChecked(True)

        # layout
        layout = QFormLayout()
        #layout.addWidget(self.radio_masc)
        #layout.addWidget(self.radio_femi)
        layout.addRow(self.radio_masc, self.radio_femi)
        self.setLayout(layout)
    
    def get_genero(self):
        '''
        retornar o genero selecionado.
        '''
        genero = self.radio_masc.text() if self.radio_masc.isChecked() else self.radio_femi.text()
        return genero

# overview
if __name__ == '__main__':
    import sys
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication
    from window import Window


    app = QApplication([])
    app.setFont(QFont('Georgia', 14))

    programa = Window()
    programa.show()
    
    programa.setCentralWidget(Genero())
    print(programa.centralWidget().get_genero())

    sys.exit(app.exec_())
