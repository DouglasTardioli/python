
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        #configuração inicial
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        #TITULo da Janela
        self.setWindowTitle('Calculadora Python')

        
        
    def adjustFixedSize(self):
        #Ultima coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def addToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)