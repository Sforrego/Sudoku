import sys
from PyQt5.QtGui import (QPixmap, QTransform, QIcon, QImage, QBrush,
                         QPalette)
from PyQt5.QtCore import QTimer, pyqtSignal, QSize, Qt
from PyQt5.QtWidgets import (QLabel, QWidget,  QApplication, QLineEdit,
                             QPushButton, QVBoxLayout, QDesktopWidget, QMainWindow)
from PyQt5.QtTest import QTest

from classes import Board
from BackEnd import board_loader

class ClickLabel(QLabel):
    #intento de label clickeable
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class App(QWidget):
    def __init__(self, board):
        super().__init__()
        self.title = 'Sudoku'
        self.left = 10
        self.top = 30

        dw = QDesktopWidget()
        self.width = dw.width()
        self.height = dw.height()

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #number to place
        self.selected_num = 0

        #background white
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        #empty grid
        self.grid_label = QLabel(self)
        self.grid_size = 400
        self.num_size = 400/9 #para el tamaño de los numeros
        self.grid_pixmap = QPixmap('Assets/background6.png').scaled(self.grid_size,
                                                                self.grid_size)
        self.grid_label.setPixmap(self.grid_pixmap)
        self.resize(self.grid_size+200,self.grid_size)
        self.num_img = {i:f'Assets/nums4/{i}.png' for i in range(0,10) }
        self.num_img2 = {i:f'Assets/nums3/{i}.png' for i in range(0,10) }

        #buttons
        self.buttons = {}
        for i in range(9):
            self.buttons[i] = QPushButton("", self)
            self.buttons[i].setCheckable(True)
            self.buttons[i].clicked[bool].connect(self.make_selected(i+1))
            self.buttons[i].setIcon(QIcon(self.num_img2[i+1]))
            #self.buttons[i]1.setIconSize(QSize(24,24))
            self.buttons[i].setGeometry(420, 20+41*i, 60, 30)
            self.buttons[i].show()

        #initialize board
        self.board = Board(board)

        self.cells = {}

        for i in range(9):
            for j in range(9):
                num = self.board.board[i][j]
                #si no viene  en el original se puede cambiar
                if num == 0:
                    self.cells[(i,j)] =  ClickLabel(self)
                    self.cells[(i,j)].clicked.connect(self.on_product_clicked)
                else:
                    # label = QLabel(self)
                    # label.move(self.num_size*0.9*i+25, self.num_size*0.9*j+22)
                    # pixmap2 = QPixmap("Assets/color.png").scaled(self.num_size*0.7,self.num_size*0.7)
                    # label.setPixmap(pixmap2)
                    # label.show()
                    self.cells[(i,j)] =  QLabel(self)

                # x width y altura
                self.cells[(i,j)].move(self.num_size*0.9*i+25, self.num_size*0.9*j+23)
                pixmap = QPixmap(self.num_img[num]).scaled(self.num_size*0.7,
                                                            self.num_size*0.7)
                self.cells[(i,j)].setPixmap(pixmap)


                self.cells[(i,j)].show()



        self.show()

    def on_product_clicked(self):
        label = self.sender()
        pixmap = QPixmap(self.num_img2[self.selected_num]).scaled(self.num_size*0.7,
                                                    self.num_size*0.7)
        label.setPixmap(pixmap)
        label.show()

    def make_selected(self, num):
        def selected():
            if self.selected_num == 0:
                self.selected_num = num
            else:
                self.selected_num = 0
        return selected

    def mousePressEvent(self, event):
        print(f"x:{event.x()} y:{event.y()}")

if __name__ == '__main__':
    board = sys.argv[1]
    app = QApplication(sys.argv)
    board = board_loader(board)
    ventana = App(board)

    app.exec_()
