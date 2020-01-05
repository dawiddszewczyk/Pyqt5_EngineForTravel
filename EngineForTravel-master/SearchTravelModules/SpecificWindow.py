import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap, QImage, QPalette, QPainter, QColor, QBrush, QFontDatabase
from PyQt5.QtCore import QSize, QRect
import mysql.connector
from SearchTravelModules import DatabaseQuery, UserConfig, SavePDF, MainApplication, BasketModule

class SpecificWindow(QWidget):
        # <----------- nick,UserID,Password
    def __init__(self, Basket, ID, QueryObject, OfV_Title):
        super().__init__()

        QueryObject.OfferDeatails(ID)
        self.OfferViev_Title = OfV_Title
        self.Title = QueryObject.MainDetail[0][0]
        self.Content = QueryObject.MainDetail[0][1]
        self.Country = QueryObject.MainDetail[0][2]
        self.Transport = QueryObject.Transport
        self.Prices = QueryObject.Costs
        self.ContactInfo = QueryObject.Contact
        self.TransportPrices = QueryObject.TransportCosts
        if QueryObject.Additional:
            self.AdditionalInfo = QueryObject.Additional
        self.PicturePath = []
        for tPicture in QueryObject.PicturesPath:
            if tPicture[1] == ID:
                self.PicturePath.append(tPicture[2])
        self.oBasket = Basket

        '''
        #<--------- A chars before word means type of Valiable.
        i* - int
        f* - float
        d* - double
        s* - string
        c* - char
        *IMG - image
        r* - rect 
        #<-----------
        '''

        # <--------------  Style For setStyleSheet

        self.Q_Button_Style="QPushButton { color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0); text-align: center}"
        self.Q_Label_Style = " QLabel { background-color: #84bd00;}"
        self.Q_Label_BoldStyle = " QLabel {font-weight: bold;color: #84bd00; text-align: center;}"
        self.Q_LineEdit_TextBoxStyle = "QLineEdit{border:1px solid  #383838; color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0);}"

        # <------ Initiation Font Type to fontDataBase.

        QFontDatabase.addApplicationFont("Font/DukeFill.ttf")
        QFontDatabase.addApplicationFont("Font/Focus-Medium.ttf")
        QFontDatabase.addApplicationFont("Font/Roboto-ThinItalic.ttf")

        # <------- Get Resolution on Screen and Set value to valiables.

        iscreen = QApplication.primaryScreen().grabWindow(0)

        isize = iscreen.size()
        self.WindowWidth = isize.width() * 50 / 100
        self.WindowHeight = isize.height() * 50 / 100
        self.setGeometry(self.WindowWidth / 2, self.WindowHeight / 2, self.WindowWidth, self.WindowHeight)

        # <------ dynamic valiable to set Font size
        self.__fFontSize = self.WindowHeight * 0.015
        self.__fFontSizeTitle = self.WindowHeight * 0.030

        # <-------- Background
        BackgroundTextureIMG = QImage("Img/tlo.png")
        BackgroundIMG = BackgroundTextureIMG.scaled(QSize(self.WindowHeight,self.WindowWidth))
        BackgroundPaletteIMG = QPalette()
        BackgroundPaletteIMG.setBrush(10,QBrush(BackgroundIMG))
        self.setPalette(BackgroundPaletteIMG)

        # <--- Window Without frame.
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.font = QFont()
        self.font.setFamily("DukeFill")
        self.font.setPointSize(self.__fFontSize)

        self.fontTitle = QFont()
        self.fontTitle.setFamily("DukeFill")
        self.fontTitle.setPointSize(self.__fFontSizeTitle)


        self.initUI()


    def initUI(self):

        self.Consistwindow()
        self.show()

    def paintEvent(self, e):
        self.draw = QPainter()
        self.draw.begin(self)
        self.drawRectangles()
        self.draw.end()

    def drawRectangles(self):
        # <---------- draw.drawRect(x,y,width,height)

        col = QColor(28, 28, 31)
        self.draw.setPen(col)

        #  rConsistSide
        self.draw.setBrush(QColor(28, 28, 31))
        self.draw.drawRect(self.WindowWidth * 1 / 100, self.WindowHeight * 22 / 100, self.WindowWidth * 98 /100, self.WindowHeight* 76 /100)

        # rBottomSide
        self.draw.setBrush(QColor(28, 28, 31))
        self.draw.drawRect(self.WindowWidth * 0 / 100, self.WindowHeight * 0 / 100, self.WindowWidth , self.WindowHeight * 20 /100)

        # <----END

    def Consistwindow(self):

        self.ButtonExist()
        sTitle = QLabel(self)
        sTitle.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 7 / 100,self.WindowWidth*40/100,self.WindowHeight * 5 / 100)
        sTitle.setStyleSheet(self.Q_Label_BoldStyle)
        sTitle.setText("{0}".format(self.Title))
        sTitle.setFont(self.fontTitle)

        sContent = QLabel(self)
        sContent.setGeometry(self.WindowWidth * 25 / 100, self.WindowHeight * 65 / 100, self.WindowWidth * 50 / 100, self.WindowHeight * 30 / 100)
        sContent.setStyleSheet('''QLabel {color: #84bd00;}''')
        sContent.setText("{0}".format(self.TextSpliter(sContent, self.Content)))
        sContent.setFont(self.font)

        rPhoto = QLabel(self)
        PlaceIMG = QPixmap("../OfferIMG/{0}".format(self.PicturePath[0]))
        PlaceIMG = PlaceIMG.scaled(300, 200)
        rPhoto.setPixmap(PlaceIMG)
        rPhoto.setGeometry(self.WindowWidth * 35 / 100, self.WindowHeight * 27 / 100, self.WindowWidth * 40 / 100,self.WindowHeight * 5 / 100)
        rPhoto.setStyleSheet('''QLabel {background-color: black;}''')
        rPhoto.resize(300,200)

        sTransport = QLabel(self)
        sTransport.setGeometry(self.WindowWidth * 80 / 100, self.WindowHeight * 27 / 100, self.WindowWidth * 40 / 100,self.WindowHeight * 5 / 100)
        sTransport.setStyleSheet(self.Q_Label_BoldStyle)
        sTransport.setText("Dostępne środki transportu".format(self.Content))
        sTransport.setFont(self.font)

        ChildPrice = QLabel(self)
        ChildPrice.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 27 / 100, self.WindowWidth * 20 / 100,self.WindowHeight * 5 / 100)
        ChildPrice.setStyleSheet(self.Q_Label_BoldStyle)
        ChildPrice.setText("Dzieci:  {0} zł".format(self.Prices[0][1]))
        AdultPrice = QLabel(self)
        AdultPrice.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 37 / 100, self.WindowWidth * 20 / 100,self.WindowHeight * 5 / 100)
        AdultPrice.setStyleSheet(self.Q_Label_BoldStyle)
        AdultPrice.setText("Dorośli:  {0} zł".format(self.Prices[0][0]))
        SeniorPrice = QLabel(self)
        SeniorPrice.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 47 / 100, self.WindowWidth * 20 / 100,self.WindowHeight * 5 / 100)
        SeniorPrice.setStyleSheet(self.Q_Label_BoldStyle)
        SeniorPrice.setText("Seniorzy:  {0} zł".format(self.Prices[0][2]))

        if self.Transport[0][0]:
            BusPhotoIMG = QPixmap("../SearchTravelIMG/busGreen.png")

        else:
            BusPhotoIMG = QPixmap("../SearchTravelIMG/busRED.png")
        Bus = QLabel(self)
        Bus.setPixmap(BusPhotoIMG)
        Bus.move(self.WindowWidth * 80 / 100, self.WindowHeight * 35 / 100)

        BusPrice = QLabel(self)
        BusPrice.setText("{0} zł".format(self.TransportPrices[0][0]))
        BusPrice.move(self.WindowWidth * 88 / 100, self.WindowHeight * 38 / 100)
        BusPrice.setStyleSheet(self.Q_Label_BoldStyle)

        if self.Transport[0][1]:
            TrainPhotoIMG = QPixmap("../SearchTravelIMG/trainGreen.png")
        else:
            TrainPhotoIMG = QPixmap("../SearchTravelIMG/trainRED.png")
        Train = QLabel(self)
        Train.setPixmap(TrainPhotoIMG)
        Train.move(self.WindowWidth * 80 / 100, self.WindowHeight * 48 / 100)

        TrainPrice = QLabel(self)
        TrainPrice.setText("{0} zł".format(self.TransportPrices[0][1]))
        TrainPrice.move(self.WindowWidth * 88 / 100, self.WindowHeight * 51 / 100)
        TrainPrice.setStyleSheet(self.Q_Label_BoldStyle)

        if self.Transport[0][2]:
            PlanePhotoIMG = QPixmap("../SearchTravelIMG/airplaneGreen.png")
        else:
            PlanePhotoIMG = QPixmap("../SearchTravelIMG/airplaneRED.png")
        Plane = QLabel(self)
        Plane.setPixmap(PlanePhotoIMG)
        Plane.move(self.WindowWidth * 80 / 100, self.WindowHeight * 61 / 100)

        PlanePrice = QLabel(self)
        PlanePrice.setText("{0} zł".format(self.TransportPrices[0][2]))
        PlanePrice.move(self.WindowWidth * 88 / 100, self.WindowHeight * 64 / 100)
        PlanePrice.setStyleSheet(self.Q_Label_BoldStyle)


        if self.Transport[0][3]:
            ShipPhotoIMG = QPixmap("../SearchTravelIMG/shipGreen.png")
        else:
            ShipPhotoIMG = QPixmap("../SearchTravelIMG/shipRED.png")
        Ship = QLabel(self)
        Ship.setPixmap(ShipPhotoIMG)
        Ship.move(self.WindowWidth * 80 / 100, self.WindowHeight * 74 / 100)

        ShipPrice = QLabel(self)
        ShipPrice.setText("{0} zł".format(self.TransportPrices[0][3]))
        ShipPrice.move(self.WindowWidth * 88 / 100, self.WindowHeight * 77 / 100)
        ShipPrice.setStyleSheet(self.Q_Label_BoldStyle)

        sFaktura = QPushButton('Faktura', self)
        sFaktura.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 70 / 100, self.WindowWidth * 5 / 100,self.WindowHeight * 5 / 100)
        sFaktura.setStyleSheet(self.Q_Button_Style)
        sFaktura.clicked.connect(self.FileFacturaPdf)
        sFaktura.setFont(self.font)

        sExportToPDF = QPushButton('Export to PDF', self)
        sExportToPDF.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 80 / 100, self.WindowWidth * 10 / 100,self.WindowHeight * 5 / 100)
        sExportToPDF.setStyleSheet(self.Q_Button_Style)
        sExportToPDF.clicked.connect(self.ExportToPDF)
        sExportToPDF.setFont(self.font)

        BaskedAddButton = QPushButton("Dodaj do koszyka", self)
        BaskedAddButton.setGeometry(self.WindowWidth* 10 / 100, self.WindowHeight * 90 / 100, self.WindowWidth * 10 / 100, self.WindowHeight* 5 / 100)
        BaskedAddButton.setStyleSheet(self.Q_Button_Style)
        BaskedAddButton.setFont(self.font)
        BaskedAddButton.clicked.connect(self.AddToBasket)

    def exit(self, event):
        self.close()
        self.destroy()

    def FileFacturaPdf(self):
        pass

    def ExportToPDF(self):
        self.S_PDF = SavePDF.SaveToPDF("index.html", self.Title, self.Content, 1000, "../OfferIMG/{0}".format(self.PicturePath[0]))
        self.S_PDF.show()
        self.close()

    def AddToBasket(self):
        self.addBasket = BasketModule.AddToBasketWindow(self.oBasket, self.Transport,
                                                        self.Prices, self.TransportPrices, self.OfferViev_Title)
        self.addBasket.show()

    def ButtonExist(self):
        exit = QLabel(self)
        exit.move(self.WindowWidth * 94 / 100, self.WindowHeight * 1 / 100)
        exit.resize(self.WindowWidth * 5 / 100, self.WindowHeight * 3 / 100)
        exit.setStyleSheet("QLabel { background-color : #dc143c;}")
        exit.mousePressEvent = self.exit

    def TextSpliter(self, label, ContentStr):
        sFinalResult = ""
        sTmpStr = ""

        for c in ContentStr:
            sTmpStr = sTmpStr + c
            label.setText(sTmpStr)
            width = label.fontMetrics().boundingRect(label.text()).width()
            if width >= label.width():
                Throwed = ""
                sReverse = sTmpStr[::-1]
                iTmpPos = sReverse.find(c)
                while sReverse[iTmpPos] != " ":
                    Throwed = Throwed + sReverse[iTmpPos]
                    iTmpPos += 1
                sReverse = sReverse[iTmpPos:]
                sTmpStr = sReverse[::-1]
                sTmpStr = sTmpStr + '\n'
                sFinalResult = sFinalResult + sTmpStr
                sTmpStr = "" + Throwed[::-1]

        sFinalResult = sFinalResult + sTmpStr
        return sFinalResult

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    ex = SpecificWindow()
    sys.exit(app.exec_())
