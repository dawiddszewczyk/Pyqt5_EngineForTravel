import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon,QFont,QPixmap,QImage, QPalette, QBrush,QPainter, QColor, QBrush,QFontDatabase,QSessionManager
from PyQt5.QtCore import pyqtSlot,QSize,QRect
import sqlite3
from functools import partial
from SearchTravelModules import MainApplication, DatabaseQuery, InfoWindow
import mysql.connector

class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
    # <------- Set a font to datafontbase
        QFontDatabase.addApplicationFont("Fonts/DukeFill.ttf")
        QFontDatabase.addApplicationFont("Fonts/Focus-Medium.ttf")
        QFontDatabase.addApplicationFont("Fonts/Roboto-ThinItalic.ttf")
    # <--- END

    # <-- Get a Screen Size
        self.screen = QApplication.primaryScreen().grabWindow(0)
        self.size = self.screen.size()
        self.WindowWidth = self.size.width()*50/100
        self.WindowHeight = self.size.height()*50/100

    # <---END

    # Photo On the Background
        oImage = QImage("../SearchTravelIMG/tlo.png")
        sImage = oImage.scaled(QSize(800, 500))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
    # <----END

    # Set Window Size ( x ,y ,width ,height )
        #               (420,0         , 262,5         , 840,0         , 525.0          )
        #   Window width -> 50% of screen windth, Window height -> 50% of screen height
        self.setGeometry(self.size.width()/4,self.size.height()/4, self.WindowWidth, self.WindowHeight)
    # <----END
    # Set windows Without Frame
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # <----END

    # Label which check if the Button will be press.
        exit = QLabel(self)
        exit.move(self.WindowWidth * 94 / 100, self.WindowHeight * 1 / 100)
        exit.resize(35, 15)
        exit.setStyleSheet("QLabel { background-color : #dc143c;}");
        exit.mousePressEvent = self.exit

    # <-- END

        self.initUI()

    # <-- To close window
    def exit(self, event):
        self.close()
    # To show more info about errors !
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = my_exception_hook
    # <----------END!!

    def initUI(self):

        self.ConsistWindow()
        self.show()
    # <-----Function to draw a reckt (baner,button,menu,line)
    def paintEvent(self, e):
        self.draw = QPainter()
        self.draw.begin(self)
        self.drawRectangles()
        self.draw.end()

    def drawRectangles(self):
        # <---------- draw.drawRect(x,y,width,height)

        col = QColor(28, 28, 31)
        self.draw.setPen(col)

        # Right menu
        self.draw.setBrush(QColor(28, 28, 31))
        self.draw.drawRect(self.WindowWidth*68/100, self.WindowHeight*5/100, self.WindowWidth*30/100, self.WindowHeight*90/100)

        # Cointaner
        self.draw.setBrush(QColor(28, 28, 31))
        self.draw.drawRect(self.WindowWidth*2/100, self.WindowHeight*5/100, self.WindowWidth*62/100, self.WindowHeight*90/100)

        #Green Line
        self.draw.setBrush(QColor(132,189,0))
        self.draw.drawRect(self.WindowWidth*70/100, self.WindowHeight*30/100, self.WindowWidth*25/100, 2)


    # <----END




    def ConsistWindow(self):

        __fFontSize = self.WindowHeight * 0.017

        font = QFont()
        font.setFamily("DukeFill")
        font.setPointSize(__fFontSize)

        logo = QLabel(self)
        pixmaplog = QPixmap('../SearchTravelIMG/globe.png')
        logo.setPixmap(pixmaplog)
        logo.move(self.WindowWidth*79/100,self.WindowHeight*10/100)

        minim = QLabel(self)
        minimlog = QPixmap('../SearchTravelIMG/minimize.png')
        minim.setPixmap(minimlog)
        minim.move(self.WindowWidth * 90 / 100, self.WindowHeight * 1.2 / 100)
        minim.mousePressEvent = self.minim


        self.sLabelMainContainer = QLabel(self)
        self.sLabelMainContainer.move(200, 60)
        self.sLabelMainContainer.setStyleSheet(" QLabel {font-weight: bold;color: #84bd00;}")

        textboxstyleSheet = """QLineEdit{border:1px solid  #383838; color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0);}"""



        self.textbox = QLineEdit(self)
        self.textbox.move(self.WindowWidth*75/100, self.WindowHeight*35/100)
        self.textbox.resize(140, 20)
        self.textbox.setStyleSheet(textboxstyleSheet)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(self.WindowWidth*75/100, self.WindowHeight*42/100)
        self.textbox2.resize(140, 20)
        self.textbox2.setEchoMode(QLineEdit.Password)
        self.textbox2.setStyleSheet(textboxstyleSheet)

        self.button = QPushButton('Login', self)
        self.button.setStyleSheet("QPushButton { color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0); }" )
        self.button.resize(40, 20)
        self.button.move(self.WindowWidth*75/100, self.WindowHeight*49/100)

        self.button.setToolTip('Zaloguj sie do systemu')
        self.button.clicked.connect(self.on_click)

        self.rest = QPushButton('Reset', self)
        self.rest.setStyleSheet("QPushButton { color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0); }")
        self.rest.resize(40, 20)
        self.rest.move(self.WindowWidth*81/100, self.WindowHeight*49/100)

        self.rest.setToolTip('Wyczysc dane')
        self.rest.clicked.connect(self.on_rest)


    @pyqtSlot()
    def on_click(self):
        bLoginCor = False
        textboxValue = self.textbox.text()
        textboxValue2 = self.textbox2.text()

        connection = mysql.connector.connect(user=DatabaseQuery.databaseConnection['user'], password=DatabaseQuery.databaseConnection['password'],host=DatabaseQuery.databaseConnection['host'], database=DatabaseQuery.databaseConnection['database'])
        DataBaseOperate = connection.cursor()
        query = "SELECT ID,Login,Password FROM Users WHERE Login='{0}' AND Password='{1}'".format(textboxValue,textboxValue2)
        DataBaseOperate.execute(query)

        for(ID, Login, Password) in DataBaseOperate:
            if(Login == textboxValue and Password == textboxValue2):
                bLoginCor = True
                UserID = ID

        if bLoginCor:
            self.SW = MainApplication.FirstPanel(Login, UserID, Password)
            self.SW.show()
            self.ShowStatusWindow("Zalogowano pomyślnie!")
            self.destroy()
        else:
            self.ShowStatusWindow("Błąd! Porszę wprowadzić poprawne dane!")
            self.on_rest()
        connection.close()

    def ShowStatusWindow(self, message):
        self.StatusWindow = InfoWindow.StateWindow(message)
        self.StatusWindow.show()

    @pyqtSlot()
    def on_rest(self):
        self.textbox.setText("")
        self.textbox2.setText("")

    def minim(self, event):
        self.showMinimized()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondWindow()
    sys.exit(app.exec_())