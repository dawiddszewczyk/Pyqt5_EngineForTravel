import sys, os
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont, QPixmap, QImage, QPalette, QBrush,QPainter, QColor, QBrush, QFontDatabase, QSessionManager, QFontMetrics
from PyQt5.QtCore import pyqtSlot,QSize,QRect

class StateWindow(QWidget):
    def __init__(self, Message):
        super().__init__()

        # Setting Fonts
        QFontDatabase.addApplicationFont("Fonts/DukeFill.ttf")
        QFontDatabase.addApplicationFont("Fonts/Focus-Medium.ttf")
        QFontDatabase.addApplicationFont("Fonts/Roboto-ThinItalic.ttf")
        # Setting size variable
        screen = QApplication.primaryScreen().grabWindow(0)
        self.size = screen.size()
        self.WindowWidth = self.WindowWidth(Message)+20
        self.WindowHeight = self.size.height() * 10 / 100
        # Setting styles
        self.QLabelStyle = """QLabel{color: #99cc00;font-family:DukeFill;font-size:13px; text-align: center;}"""
        self.QPushButtonStyle = """QPushButton { color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0); font-size:19px;
                                    text-align: center;}"""
        # Setting global variables
        self.Message = Message
        # Setting photo on background
        Background= QLabel(self)
        BackgroundIMG = QPixmap("../SearchTravelIMG/tlo.png")
        Background.setPixmap(BackgroundIMG)

        self.initUI()

    def initUI(self):
        # Setting position and size of window
        self.setGeometry(self.size.width()/5,self.size.height()/5,self.WindowWidth,self.WindowHeight)
        # Drawing without frames
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Show message
        self.ShowMessage()
        # Show OK button
        self.okButton()
        # Draw everything
        self.show()

    def ShowMessage(self):
        MessageLabel = QLabel(self)
        MessageLabel.setGeometry(self.WindowWidth*5/100,self.WindowHeight*8/100,self.WindowWidth*90/100,self.WindowHeight*60/100)
        MessageLabel.setStyleSheet(self.QLabelStyle)
        MessageLabel.setText(self.Message)


    def okButton(self):
        okButton = QPushButton("OK",self)
        okButton.setStyleSheet(self.QPushButtonStyle)
        okButton.setGeometry(self.WindowWidth*1/100,self.WindowHeight*75/100,self.WindowWidth,self.WindowHeight*17/100)
        okButton.clicked.connect(self.okClick)


    def okClick(self):
        self.close()
        self.destroy()

    # Function calculates window width depending on width of the string
    def WindowWidth(self, str):
        Font = QFont("DukeFill", 13)
        FontMetr = QFontMetrics(Font)
        WindowWidth = FontMetr.width(str)
        return WindowWidth

if __name__ ==  '__main__':
    app = QApplication(sys.argv)
    ex = StateWindow()
    sys.exit(app.exec_())