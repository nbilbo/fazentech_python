# coding: utf-8

from PyQt5.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.settings()
    
    def settings(self):
        self.setWindowTitle('PyQt5 Window')
        self.resize(900, 400)
