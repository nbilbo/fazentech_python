# coding: utf-8


from PyQt5.QtWidgets import QGroupBox, QFormLayout, QRadioButton, QCalendarWidget


class Inseminacao(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Inseminacao, self).__init__(*args, **kwargs)
        self.setTitle('Inseminação')
        # radio buttons
        self.radio_sim = QRadioButton(text='&sim')
        self.radio_nao = QRadioButton(text='n&ão')
        self.radio_nao.setChecked(True)

        # calendar
        self.calendario = QCalendarWidget()
        self.calendario.setVisible(False)

        # conectando o método ao botão
        self.radio_sim.toggled.connect(self.radio_changed)

        # layout
        layout = QFormLayout()
        layout.addRow(self.radio_nao, self.radio_sim)
        layout.addWidget(self.calendario)
        self.setLayout(layout)
    
    def radio_changed(self):
        '''
        Alterar a visibilidade do calendário.
        '''
        if self.radio_sim.isChecked():    
            self.calendario.setVisible(True)
        else:
            self.calendario.setVisible(False)

    def get_inseminacao(self):
        '''
        Retornar um dicionário com a data da inseminação.
        '''
        resultado = {}
        if self.radio_sim.isChecked():
            resultado['data_eua'] = self.calendario.selectedDate().toString('yyyy-MM-dd')
            resultado['data_br'] = self.calendario.selectedDate().toString('dd-MM-yyyy')
        else:
            resultado = None

        return resultado


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QFont


    app = QApplication([])
    app.setFont(QFont('Georgia', 12))

    window = QMainWindow()
    window.setCentralWidget(Inseminacao())
    window.resize(1100, 500)
    window.show()
    
    sys.exit(app.exec_())
