import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QImage, QPalette, QPainter, QColor, QBrush, QFontDatabase
from SearchTravelModules.FunctionsModule import SetFont, TextSize

class Invoice(QWidget):
    def __init__(self):
        super().__init__()
        # Setting Fonts
        QFontDatabase.addApplicationFont("Fonts/DukeFill.ttf")
        QFontDatabase.addApplicationFont("Fonts/Focus-Medium.ttf")
        QFontDatabase.addApplicationFont("Fonts/Roboto-ThinItalic.ttf")

        # Setting styles
        self.QLabelStyle = """QLabel{color: #99cc00;}"""
        self.QCheckBoxStyle = """QCheckBox{color: #99cc00;}"""
        self.QLabelStyleHeader = """QLabel{color: #99cc00; font-weight: bold;}"""
        self.QLineEditStyle = """QLineEdit{color: #99cc00; background-color: rgba(0,0,0,0); }"""
        self.QPushButtonStyle = """QPushButton { color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0); }"""

        # Setting size variable
        screen = QApplication.primaryScreen().grabWindow(0)
        self.size = screen.size()
        self.WindowWidth = self.size.width() * 50 / 100
        self.WindowHeight = self.size.height() * 60 / 100

        # Deleting frames
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Drawing UI
        self.__initUI()

    def __initUI(self):
        # Setting position and size of window
        self.setGeometry(self.size.width()/2-self.WindowWidth/2,self.size.height()/2-self.WindowHeight/2,
                         self.WindowWidth,self.WindowHeight)

        # Drawing form
        self.__MainRect()
        # Drawing top bar
        self.__TopBar()
        # Drawing exit button
        self.__ExitButton()
        # Drawing seller deatils
        self.__SellerDetails()
        # Drawing purchaser detail
        self.__PurchDetails()
        # Show window
        self.show()

    def __MainRect(self):
        QL_MainRect = QLabel(self)
        QL_MainRect.setGeometry(0, 0, self.WindowWidth, self.WindowHeight)
        QL_MainRect.setStyleSheet("QLabel { background-color : #181920;}")

    def __TopBar(self):
        QL_TopBar = QLabel(self)
        QL_TopBar.setGeometry(0,0, self.WindowWidth, self.WindowHeight*5/100)
        QL_TopBar.setStyleSheet("QLabel { background-color : #137514;}")
        QL_TopBar.mousePressEvent = self.Click

    def __ExitButton(self):
        QL_Exit = QLabel(self)
        QL_Exit.setGeometry(self.WindowWidth*94/100, self.WindowHeight*1/100,
                          self.WindowWidth * 5/100, self.WindowHeight * 3/100)
        QL_Exit.setStyleSheet("QLabel { background-color : #dc143c;}")
        QL_Exit.mousePressEvent = self.__exit

    def __SellerDetails(self):
        QL_CompDetail = QLabel(self)
        QL_CompDetail.setStyleSheet(self.QLabelStyleHeader)
        QL_CompDetail.setText("Dane firmy")
        QL_CompDetail.move(self.WindowWidth*5/100, self.WindowHeight*7/100)

        SellDetQL = self.CreateQL(["Nazwa firmy:", "Adres:", "Numer telefonu:", "NIP:", "Oddział banku:", "Numer rachunku:"],
                          self.WindowWidth*5/100, self.WindowHeight*10/100, 0, self.WindowHeight*3/100)

        for QL in SellDetQL:
            QL.show()

        SellDetQLE = self.CreateQLE(len(SellDetQL), 0, 0, self.WindowWidth*1/100, 4, SellDetQL)

        for QLE in SellDetQLE:
            QLE.show()

    def __PurchDetails(self):
        QL_PurchDetails = QLabel(self)
        QL_PurchDetails.setStyleSheet(self.QLabelStyleHeader)
        QL_PurchDetails.setText("Dane odbiorcy")
        QL_PurchDetails.move(self.WindowWidth*50/100, self.WindowHeight*7/100)

        QCB_Priv = QCheckBox("Osoba prywatna", self)
        QCB_Priv.move(QL_PurchDetails.x()+QL_PurchDetails.width()+9, self.WindowHeight*6.5/100)
        QCB_Priv.setStyleSheet(self.QCheckBoxStyle)
        # TUEJ
        QCB_Priv.stateChanged.connect(lambda: self.C())

        QCB_Comp = QCheckBox("Firma", self)
        QCB_Comp.move(QCB_Priv.x()+QCB_Priv.width()+40, self.WindowHeight*6.5/100)
        QCB_Comp.setStyleSheet(self.QCheckBoxStyle)

    def C(self):
        print("H")

    def CreateQL(self, LabelText, StartX, StartY, mVx, mVy):
        LabelList = []

        for n in LabelText:
            QL_TMP = QLabel(self)
            QL_TMP.setStyleSheet(self.QLabelStyle)
            QL_TMP.setFixedWidth(TextSize(n, self.WindowHeight*0.02))
            QL_TMP.setText(n)
            QL_TMP.move(StartX, StartY)
            QL_TMP.setFont(SetFont(self.WindowHeight*0.02))
            LabelList.append(QL_TMP)
            StartX += mVx
            StartY += mVy

        return LabelList

    def CreateQLE(self, Amount, StartX, StartY, mVx, mVy, QL_List = None):
        LabelList = []

        for n in range(0, Amount):
            QLE_TMP = QLineEdit(self)
            QLE_TMP.setStyleSheet(self.QLineEditStyle)
            if QL_List:
                QLE_TMP.move(QL_List[n].width()+QL_List[n].x()+mVx, QL_List[n].y()-mVy)
            else:
                QLE_TMP.move(StartX, StartY)
                StartX += mVx
                StartY += mVy
            QLE_TMP.setFont(SetFont(self.WindowHeight*0.02))
            LabelList.append(QLE_TMP)

        return LabelList


    def __exit(self, ev):
        self.close()
        self.destroy()

    # --------------------------------------------------------------------- DEBUG
    def Click(self, ev):
        print("Clicked")
        print("X {} Y {}".format(ev.x(), ev.y()))

    def mouseMoveEvent(self, QMouseEvent):
        print("Mouse mME X {} Y {}".format(QMouseEvent.x(), QMouseEvent.y()))

if __name__ ==  '__main__':
    app = QApplication(sys.argv)
    ex = Invoice()
    sys.exit(app.exec_())