import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QBoxLayout
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("ACM_PL")
        
        widget = Color('black')
        self.setCentralWidget(widget)

class Color(QWidget):

    def __init__(self, color):
        
        super(Color, self).__init__()
        
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


def App():
    app = QApplication(sys.argv)
    window = MainWindow()
    #box = QBoxLayout(window)


    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    App()

