import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QDialog, 
    QHBoxLayout, 
    QPushButton,
    QLabel,
    QVBoxLayout,
    QFileDialog        
)

from PyQt6.QtGui import QPalette, QColor, QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        
        super(MainWindow, self).__init__()

        self.setWindowTitle("ACM_PL")
        #self.resize(1280, 860)

        main_layout = QHBoxLayout()

        self.image_label = QLabel('Selected Image Will Appear Here!')
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.browse_button = QPushButton('Load Image')
        self.browse_button.clicked.connect(self.browse_image)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.image_label)
        input_layout.addWidget(self.browse_button)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(Color('black'))

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)

    def browse_image(self):
        #options = QFileDialog.Options()
        #options |= QFileDialog.Option.ReadOnly

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter('Images (*.png *.jpg *.bmp *.gif *.jpeg)')

        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                image_path = file_paths[0]
                self.show_selected_image(image_path)

    def show_selected_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(False)
        

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


    window.showFullScreen()
    sys.exit(app.exec())

if __name__ == '__main__':

    App()

