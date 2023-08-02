import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from display import Display
from info import Info
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from style import setupTheme


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    
    #define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    
    #Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToLayout(info)
    #Display
    display = Display()
    display.setPlaceholderText('Digite os valores')
    window.addToLayout(display)


    window.adjustFixedSize()
    window.show()
    app.exec()