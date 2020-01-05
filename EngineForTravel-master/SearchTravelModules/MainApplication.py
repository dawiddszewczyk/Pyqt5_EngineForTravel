import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap, QImage, QPalette, QPainter, QColor, QBrush, QFontDatabase
from PyQt5.QtCore import QSize, QRect
import mysql.connector
from SearchTravelModules import DatabaseQuery, UserConfig, SpecificWindow, BasketModule

class FirstPanel(QWidget):
        # <----------- nick,UserID,Password
    def __init__(self, Login="Jan", UserID=4, Password="JanK"):
        super().__init__()

        self.i = 0
        self.counter = 0

        self.sLogin = Login
        self.suID = UserID
        self.sPassword = Password

        self.Checker = False
        self.PrevButton = None

        self.D = DatabaseQuery.Data()
        self.D.OfferView()
        self.D.DownloadPictures()

        self.oBasket = BasketModule.Basket()
        self.oBasket.Test()

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
        self.__fFontSize = self.WindowHeight * 0.017
        self.__fFontSizeFilters = self.WindowHeight * 0.014

        # <-------- Background
        BackgroundTextureIMG = QImage("Img/tlo.png")
        BackgroundIMG = BackgroundTextureIMG.scaled(QSize(self.WindowHeight,self.WindowWidth))
        BackgroundPaletteIMG = QPalette()
        BackgroundPaletteIMG.setBrush(10,QBrush(BackgroundIMG))
        self.setPalette(BackgroundPaletteIMG)

        # <--- Window Without frame.
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        self.initUI()


    def initUI(self):

        self.Consistwindow()
        self.printBeforeButton()
        self.printNextButton()
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

        #  rLeftSide
        self.draw.setBrush(QColor(28, 28, 31))
        self.draw.drawRect(self.WindowWidth * 0 / 100, self.WindowHeight * 0 / 100, self.WindowWidth * 25 /100, self.WindowHeight)

        # rBottomSide
        self.draw.setBrush(QColor(28, 28, 31))
        self.draw.drawRect(self.WindowWidth * 0 / 100, self.WindowHeight * 0 / 100, self.WindowWidth , self.WindowHeight * 20 /100)

        # <----END

    def Consistwindow(self):
        self.QueryResult = self.D.ViewInformation


        # <------- Variabels To device search / printnext / printbefore

        self.TaskRect = []  # Rect task background
        self.TitleLabel = []  # Task title
        self.TaskContent = []  # Task contents
        self.Photos = [] # Store photos
        self.y = 3.4              # Number to Set Position on rect
        self.Num = 1
        self.Number = 1
        self.RowCounter = 0  # Count displayed objects (tasks)
        self.LastPrint = len(self.D.ViewInformation) % 4  # Number of last object to print
        self.PrintAmount = len(self.D.ViewInformation) // 4  # Number of full 4-objects to print
        self.BeforeCounter = -1
        self.bPrintNext = True
        self.BeforeLastPrint = False

        self.FilterDictionary = {"Country": "",
                                 "PriceSort": "",
                                 "Transport": [0, 0, 0, 0]
                                 }

        # <---- Run First time list of thing
        self.printNext(1)

        # <--- For responsive text
        self.font = QFont()
        self.font.setFamily("DukeFill")
        self.font.setPointSize(self.__fFontSize)

        self.ButtonFiltersFont = QFont()
        self.ButtonFiltersFont.setFamily("DukeFill")
        self.ButtonFiltersFont.setPointSize(self.__fFontSizeFilters)

        # Function which check if the Button Exit be press.
        self.ButtonExist()

        sUserName = QLabel(self)
        sUserName.setGeometry(self.WindowWidth * 70 / 100, self.WindowHeight * 5 / 100,self.WindowWidth * 15 / 100,self.WindowHeight * 5 / 100)
        sUserName.setStyleSheet(self.Q_Label_BoldStyle)
        sUserName.setText("Witaj {0}".format(self.sLogin))
        sUserName.setFont(self.font)

        sUserConfig = QPushButton('Zmień ustawienia', self)
        sUserConfig.setStyleSheet(self.Q_Button_Style)
        sUserConfig.setGeometry(self.WindowWidth * 66 / 100, self.WindowHeight * 10 / 100, self.WindowWidth * 13 / 100,self.WindowHeight * 5 / 100)
        sUserConfig.setToolTip('Zmień ustawienia')
        sUserConfig.clicked.connect(self.sUserConfig_click)
        sUserConfig.setFont(self.font)

        rLogoUser = QLabel(self)
        rLogoUser.setGeometry(self.WindowWidth * 80 / 100, self.WindowHeight * 4 / 100,self.WindowWidth * 15 / 100,self.WindowHeight * 5 / 100)
        rLogoUser.setStyleSheet(self.Q_Label_Style)
        rLogoUser.resize(self.WindowWidth*8/100, self.WindowWidth*8/100)

        BasketIMG = QLabel(self)
        BasketIMGpixmap = QPixmap("../SearchTravelIMG/basket.png")
        BasketIMG.setPixmap(BasketIMGpixmap)
        BasketIMG.move(self.WindowWidth*90/100, self.WindowHeight*6/100)
        BasketIMG.mousePressEvent = self.BasketContent

        rGreenLine = QLabel(self)
        rGreenLine.setGeometry(self.WindowWidth * 3 / 100, self.WindowHeight * 20 / 100, self.WindowWidth * 19 / 100,self.WindowHeight * 0.3/ 100)
        rGreenLine.setStyleSheet(self.Q_Label_Style)

        GlobeIMG = QLabel(self)
        GlobeIMGpixmap = QPixmap("../SearchTravelIMG/globe.png")
        GlobeIMG.setPixmap(GlobeIMGpixmap)
        GlobeIMG.move(self.WindowWidth * 3 / 100, self.WindowHeight * 4 / 100)

        TitleIMG = QLabel(self)
        TitleIMGpixmap = QPixmap("../SearchTravelIMG/log.png")
        TitleIMG.setPixmap(TitleIMGpixmap)
        TitleIMG.move(self.WindowWidth * 10 / 100, self.WindowHeight * 3 / 100)

        sSearchTextBox = QLineEdit( self)
        sSearchTextBox.move(self.WindowWidth * 3.4 / 100, self.WindowHeight * 25 / 100)
        sSearchTextBox.resize(self.WindowWidth * 18 / 100, self.WindowHeight * 4 / 100)
        sSearchTextBox.setStyleSheet(self.Q_LineEdit_TextBoxStyle)

        rSearchBottom = QPushButton('Szukaj',self)
        rSearchBottom.move(self.WindowWidth * 10 / 100, self.WindowHeight * 30 / 100)
        rSearchBottom.resize(self.WindowWidth * 15 / 100, self.WindowHeight * 4 / 100)
        rSearchBottom.setStyleSheet(self.Q_Button_Style)
        rSearchBottom.setToolTip('Szukaj')
        rSearchBottom.setFont(self.font)
        rSearchBottom.clicked.connect(lambda: self.FilterSearch(sSearchTextBox.text()))

        # Filters section
        # Price Label
        sPriceLabel = QLabel(self)
        sPriceLabel.setGeometry(self.WindowWidth * 1 / 100, self.WindowHeight * 35 / 100, self.WindowWidth * 10/100, self.WindowHeight* 5/100)
        sPriceLabel.setStyleSheet(self.Q_Label_BoldStyle)
        sPriceLabel.setFont(self.font)
        sPriceLabel.setText("Cena:")

        # Children decreasing
        sChildMaxButt = QPushButton(self)
        sChildMaxButt.setGeometry(self.WindowWidth * 5.4 / 100, self.WindowHeight * 35 / 100, self.WindowWidth * 9.8/100, self.WindowHeight* 5/100)
        sChildMaxButt.setText("Dzieci malejąco")
        sChildMaxButt.setStyleSheet(self.Q_Button_Style)
        sChildMaxButt.setFont(self.ButtonFiltersFont)
        sChildMaxButt.clicked.connect(lambda: self.FilterButtonClicked(sChildMaxButt, "Child MAX"))

        # Children increasing
        sChildMinButt = QPushButton(self)
        sChildMinButt.setGeometry(self.WindowWidth * 15.4 / 100, self.WindowHeight * 35 / 100, self.WindowWidth * 9.8/100, self.WindowHeight* 5/100)
        sChildMinButt.setText("Dzieci rosnąco")
        sChildMinButt.setStyleSheet(self.Q_Button_Style)
        sChildMinButt.setFont(self.ButtonFiltersFont)
        sChildMinButt.clicked.connect(lambda: self.FilterButtonClicked(sChildMinButt, "Child MIN"))

        # Adult decreasing
        sAdultMaxButt = QPushButton(self)
        sAdultMaxButt.setGeometry(self.WindowWidth * 5.4 / 100, self.WindowHeight * 41 / 100, self.WindowWidth * 9.8/100, self.WindowHeight* 5/100)
        sAdultMaxButt.setText("Dorośli malejąco")
        sAdultMaxButt.setStyleSheet(self.Q_Button_Style)
        sAdultMaxButt.setFont(self.ButtonFiltersFont)
        sAdultMaxButt.clicked.connect(lambda: self.FilterButtonClicked(sAdultMaxButt, "Adult MAX"))

        # Adult increasing
        sAdultMinButt = QPushButton(self)
        sAdultMinButt.setGeometry(self.WindowWidth * 15.4 / 100, self.WindowHeight * 41 / 100, self.WindowWidth * 9.8/100, self.WindowHeight* 5/100)
        sAdultMinButt.setText("Dorośli rosnąco")
        sAdultMinButt.setStyleSheet(self.Q_Button_Style)
        sAdultMinButt.setFont(self.ButtonFiltersFont)
        sAdultMinButt.clicked.connect(lambda: self.FilterButtonClicked(sAdultMinButt, "Adult MIN"))

        # Senior decreasing
        sSeniorMaxButt = QPushButton(self)
        sSeniorMaxButt.setGeometry(self.WindowWidth * 5.4 / 100, self.WindowHeight * 47 / 100, self.WindowWidth * 9.8/100, self.WindowHeight* 5/100)
        sSeniorMaxButt.setText("Seniorzy malejąco")
        sSeniorMaxButt.setStyleSheet(self.Q_Button_Style)
        sSeniorMaxButt.setFont(self.ButtonFiltersFont)
        sSeniorMaxButt.clicked.connect(lambda: self.FilterButtonClicked(sSeniorMaxButt, "Senior MAX"))

        # Senior increasing
        sSeniorMinButt = QPushButton(self)
        sSeniorMinButt.setGeometry(self.WindowWidth * 15.4 / 100, self.WindowHeight * 47 / 100, self.WindowWidth * 9.8/100, self.WindowHeight* 5/100)
        sSeniorMinButt.setText("Seniorzy rosnąco")
        sSeniorMinButt.setStyleSheet(self.Q_Button_Style)
        sSeniorMinButt.setFont(self.ButtonFiltersFont)
        sSeniorMinButt.clicked.connect(lambda: self.FilterButtonClicked(sSeniorMinButt, "Senior MIN"))

        # Transport label
        sTransport = QLabel(self)
        sTransport.setGeometry(self.WindowWidth * 1 / 100, self.WindowHeight * 54 / 100, self.WindowWidth * 20 / 100,
                               self.WindowHeight * 5 / 100)
        sTransport.setStyleSheet(self.Q_Label_BoldStyle)
        sTransport.setFont(self.font)
        sTransport.setText("Dostępne środki transportu:")

        # Bus
        sBusChbx = QCheckBox("Bus", self)
        sBusChbx.setGeometry(self.WindowWidth * 1 / 100, self.WindowHeight * 59 / 100, self.WindowWidth * 10 / 100,
                               self.WindowHeight * 5 / 100)
        sBusChbx.setFont(self.font)
        sBusChbx.stateChanged.connect(lambda: self.FilterCheckBox(sBusChbx, 0))

        # Train
        sTrainChbx = QCheckBox("Pociąg", self)
        sTrainChbx.setGeometry(self.WindowWidth * 11 / 100, self.WindowHeight * 59 / 100, self.WindowWidth * 10 / 100,
                               self.WindowHeight * 5 / 100)
        sTrainChbx.setFont(self.font)
        sTrainChbx.stateChanged.connect(lambda: self.FilterCheckBox(sTrainChbx, 1))

        # Plane
        sPlaneChbx = QCheckBox("Samolot", self)
        sPlaneChbx.setGeometry(self.WindowWidth * 1 / 100, self.WindowHeight * 69 / 100, self.WindowWidth * 10 / 100,
                               self.WindowHeight * 5 / 100)
        sPlaneChbx.setFont(self.font)
        sPlaneChbx.stateChanged.connect(lambda: self.FilterCheckBox(sPlaneChbx, 2))

        # Schip
        sSchipChbx = QCheckBox("Statek", self)
        sSchipChbx.setGeometry(self.WindowWidth * 11 / 100, self.WindowHeight * 69 / 100, self.WindowWidth * 10 / 100,
                               self.WindowHeight * 5 / 100)
        sSchipChbx.setFont(self.font)
        sSchipChbx.stateChanged.connect(lambda: self.FilterCheckBox(sSchipChbx, 3))

        # Clear filters button
        sClearButt = QPushButton(self)
        sClearButt.setGeometry(self.WindowWidth * 10 / 100, self.WindowHeight * 75 / 100, self.WindowWidth * 14/100, self.WindowHeight* 5/100)
        sClearButt.setText("Resetuj ustawienia")
        sClearButt.setStyleSheet(self.Q_Button_Style)
        sClearButt.setFont(self.font)
        sClearButt.clicked.connect(lambda: self.ClearFilters([sChildMaxButt,sChildMinButt,sAdultMaxButt,
                                                              sAdultMinButt,sSeniorMaxButt,sSeniorMinButt],
                                                             [sBusChbx, sTrainChbx, sPlaneChbx, sSchipChbx]))

        # End of Filters section

    def exit(self, event):
        self.close()
        self.destroy()


    def printBeforeButton(self):
        rBeforeButton = QPushButton('Poprzednie', self)
        rBeforeButton.move(self.WindowWidth * 83 / 100, self.WindowHeight * 96 / 100)
        rBeforeButton.clicked.connect(self.printBefore)
        rBeforeButton.setStyleSheet(self.Q_Button_Style)
        rBeforeButton.setFont(self.font)

    def printNextButton(self):
        rNextButton = QPushButton('Nastepne', self)
        rNextButton.move(self.WindowWidth * 90 / 100, self.WindowHeight * 96 / 100)
        rNextButton.clicked.connect(self.printNext)
        rNextButton.setStyleSheet(self.Q_Button_Style)
        rNextButton.setFont(self.font)

    def printNext(self, event):
        if self.bPrintNext:
            if not self.PrintAmount:
                if self.RowCounter >= 4:
                    for k in range(self.RowCounter - 4, self.RowCounter):
                        # self.TaskRect[0].hide()
                        self.TaskRect[0].setStyleSheet("QLabel {background-color: black; }")
                        del (self.TaskRect[0])
                        self.TitleLabel[0].hide()
                        del (self.TitleLabel[0])
                        self.TaskContent[0].hide()
                        del (self.TaskContent[0])
                        self.y = 3.4
                        self.Number = 1
                        self.Num = 1
                for n in range(self.RowCounter, self.LastPrint + self.RowCounter):
                    self.addLabel(self.QueryResult[n][1], self.QueryResult[n][2], self.QueryResult[n][0])
                    self.TaskID = self.QueryResult[n][0]
                self.RowCounter += self.LastPrint
                self.bPrintNext = False
                self.BeforeLastPrint = True
            else:
                if self.RowCounter >= 4:
                    for k in range(self.RowCounter - 4, self.RowCounter):
                        # self.TaskRect[0].hide()
                        self.TaskRect[0].setStyleSheet("QLabel {background-color: black; }")
                        del (self.TaskRect[0])
                        self.TitleLabel[0].hide()
                        del (self.TitleLabel[0])
                        self.TaskContent[0].hide()
                        del (self.TaskContent[0])
                        self.y = 3.4
                        self.Number = 1
                        self.Num = 1
                for n in range(self.RowCounter, self.RowCounter + 4):
                    self.addLabel(self.QueryResult[n][1], self.QueryResult[n][2], self.QueryResult[n][0])
                self.RowCounter += 4
                self.PrintAmount -= 1
            self.BeforeCounter += 1


    def printBefore(self, event):
        if self.BeforeCounter:
            if self.BeforeLastPrint:
                for k in range(self.RowCounter - 1, self.RowCounter - 1 - self.LastPrint, -1):
                    # self.TaskRect[0].hide()
                    self.TaskRect[0].setStyleSheet("QLabel {background-color: black; }")
                    del (self.TaskRect[0])
                    self.TitleLabel[0].hide()
                    del (self.TitleLabel[0])
                    self.TaskContent[0].hide()
                    del (self.TaskContent[0])
                    self.y = 3.4
                    self.Number = 1
                    self.Num = 1
                self.RowCounter -= self.LastPrint
                self.BeforeLastPrint = False
            else:
                for k in range(self.RowCounter - 4, self.RowCounter):
                    #self.TaskRect[0].hide()
                    self.TaskRect[0].setStyleSheet("QLabel {background-color: black; }")
                    del (self.TaskRect[0])
                    self.TitleLabel[0].hide()
                    del (self.TitleLabel[0])
                    self.TaskLabel[0].hide()
                    del (self.TaskContent[0])
                    self.y = 3.4
                    self.Number = 1
                    self.Num = 1
                self.RowCounter -= 4
                self.PrintAmount += 1
            for n in range(self.RowCounter - 4, self.RowCounter):
                self.addLabel(self.QueryResult[n][1], self.QueryResult[n][2], self.QueryResult[n][0])
            self.BeforeCounter -= 1
            self.bPrintNext = True

    def addLabel(self, Title, contain, TaskID):
        rect = QPushButton(self)
        rect.resize(self.WindowWidth * 35 / 100, self.WindowHeight * 37/ 100)
        rect.move(self.WindowWidth * 26 / 100*self.Num,self.Number + 1 + 3.4 *self.WindowHeight * 6.3 / 100)
        rect.setStyleSheet("QPushButton {background-color: rgba(28, 28, 31); } QPushButton:hover { border: 0.5px solid #84bd00; }")
        rect.clicked.connect(lambda: self.printClicked(1, TaskID, Title))
        self.TaskRect.append(rect)

        title = QLabel("{0} \n ".format(Title), self)
        title.setStyleSheet(" QLabel {color: #84bd00;}")
        title.move(rect.x()+self.WindowWidth*2/100,self.Number + 11 + 3.4 * self.WindowHeight * 6.3 / 100)
        self.TitleLabel.append(title)

        PicturePath = []
        for tPicture in self.D.PicturesPath:
            if tPicture[1] == TaskID:
                print(tPicture)
                PicturePath.append(tPicture[2])

        Photo1 = QLabel(self)
        Photo1IMG = QPixmap("../OfferIMG/{0}".format(PicturePath[0]))
        Photo1IMG = Photo1IMG.scaled(self.WindowWidth*8/100, self.WindowWidth*8/100)
        Photo1.setPixmap(Photo1IMG)
        Photo1.setGeometry(rect.x()+self.WindowWidth*2/100,
                           self.Number + 11 + 3.4 * self.WindowHeight * 7.6 / 100,
                           self.WindowWidth * 8 / 100, self.WindowWidth*8/100)
        Photo1.setStyleSheet('''QLabel {background-color: red;}''')
        self.Photos.append(Photo1)

        print("Photo1 x -> %s" % Photo1.x())
        print("Proto1 y -> %s" % Photo1.y())

        Photo2 = QLabel(self)
        Photo2IMG = QPixmap("../OfferIMG/{0}".format(PicturePath[1]))
        Photo2IMG = Photo2IMG.scaled(self.WindowWidth*8/100, self.WindowWidth*8/100)
        Photo2.setPixmap(Photo2IMG)
        Photo2.setGeometry(Photo1.x()+Photo1.width()+self.WindowWidth*2/100, self.Number + 11 + 3.4 * self.WindowHeight * 7.6 / 100,
                           self.WindowWidth * 8 / 100, self.WindowWidth*8/100)
        Photo2.setStyleSheet('''QLabel {background-color: red;}''')
        self.Photos.append(Photo2)

        Photo3 = QLabel(self)
        Photo3IMG = QPixmap("../OfferIMG/{0}".format(PicturePath[2]))
        Photo3IMG = Photo3IMG.scaled(self.WindowWidth*8/100, self.WindowWidth*8/100)
        Photo3.setPixmap(Photo3IMG)
        Photo3.setGeometry(Photo2.x()+Photo2.width()+self.WindowWidth*2/100, self.Number + 11 + 3.4 * self.WindowHeight * 7.6 / 100,
                           self.WindowWidth * 8 / 100, self.WindowWidth*8/100)
        Photo3.setStyleSheet('''QLabel {background-color: red;}''')
        self.Photos.append(Photo3)

        content = QLabel(self)
        content.setStyleSheet(" QLabel {color: #84bd00;}")
        content.move(rect.x()+self.WindowWidth*2/100, self.Number + 41 + 3.2 * self.WindowHeight * 10.3 / 100)
        content.setGeometry(QRect(content.x(), content.y(), self.WindowWidth * 30 / 100, content.height()+50))
        content.setText(self.TextSpliter(content, contain))
        self.TaskContent.append(content)
        self.y += 3
        rect.show()
        title.show()
        content.show()
        Photo1.show()
        Photo2.show()
        Photo3.show()
        self.Num += 1.45
        if self.Num >= 3:
           self.Num = 1
           self.Number = self.WindowHeight * 40 / 100

    def printClicked(self, event, TaskID, Title):
        self.StatusWindow = SpecificWindow.SpecificWindow(self.oBasket, TaskID, self.D, Title)
        self.StatusWindow.show()


    def FilterButtonClicked(self, Button, SortType=""):
        if self.Checker:
            self.PrevButton.setStyleSheet(self.Q_Button_Style)
        else:
            self.Checker = True
        self.PrevButton = Button
        Button.setStyleSheet("QPushButton { color:rgb(132,189,0); background-color: rgb(35, 30, 45); text-align: center}")
        self.FilterDictionary['PriceSort'] = SortType

    def FilterCheckBox(self, ChkBox,Index=0):
        if ChkBox.isChecked() == True:
            self.FilterDictionary["Transport"][Index] = 1
        if ChkBox.isChecked() == False:
            self.FilterDictionary["Transport"][Index] = 0

    def ClearFilters(self, lButt, lChkBox):
        for n in lButt:
            n.setStyleSheet(self.Q_Button_Style)

        for n in lChkBox:
            n.setChecked(False)

        self.FilterDictionary = {"Country": "",
                                 "PriceSort": "",
                                 "Transport": [0, 0, 0, 0]
                                 }

    def FilterSearch(self, Country):
        for k in range(len(self.TitleLabel)):
            self.TaskContent[0].hide()
            del(self.TaskContent[0])
            self.TitleLabel[0].hide()
            del(self.TitleLabel[0])
            self.TaskRect[0].setStyleSheet("QPushButton {background-color: black; border-style: none}")
            del(self.TaskRect[0])
            for n in range(3):
                self.Photos[0].hide()
                del(self.Photos[0])

        self.FilterDictionary['Country'] = Country
        #filtredD = DatabaseQuery.Data()
        self.D.Filters(self.FilterDictionary)
        self.QueryResult = self.D.FilteredResult

        self.y = 3.4              # Number to Set Position on rect
        self.Num = 1
        self.Number = 1
        self.RowCounter = 0  # Count displayed objects (tasks)
        self.LastPrint = len(self.D.FilteredResult) % 4  # Number of last object to print
        self.PrintAmount = len(self.D.FilteredResult) // 4  # Number of full 4-objects to print
        self.BeforeCounter = -1
        self.bPrintNext = True
        self.BeforeLastPrint = False


        self.printNext(1)
        print("Filtred -------------------------------------- ")
        print(self.Photos)
        print("Photo list len: %s" % self.Photos)

    def ButtonExist(self):
        exit = QLabel(self)
        exit.move(self.WindowWidth * 94 / 100, self.WindowHeight * 1 / 100)
        exit.resize(self.WindowWidth * 5 / 100, self.WindowHeight * 3 / 100)
        exit.setStyleSheet("QLabel { background-color : #dc143c;}");
        exit.mousePressEvent = self.exit

    def sUserConfig_click(self):
        self.StatusWindow = UserConfig.UserConfigWindow(self.suID,self.sLogin,self.sPassword)
        self.StatusWindow.show()

    def TextSpliter(self, label, ContentStr):
        # Variable which store string after split
        sFinalResult = ""
        # Variable which store temporary line
        sTmpStr = ""

        # Loop which reading every single one char
        for c in ContentStr:
            # Adding the char to variable
            sTmpStr = sTmpStr + c
            # Inserting temporary line to label
            label.setText(sTmpStr)
            # Saving text width from label in variable (pixels)
            width = label.fontMetrics().boundingRect(label.text()).width()

            # Check if text width is grater than label width
            if width >= label.width():
                # Variable for rejected chars
                Throwed = ""
                # Variable which store reverse temporary line
                sReverse = sTmpStr[::-1]
                # Variale which store index of last char
                iTmpPos = sReverse.find(c)
                # Loop work until char isn't equal blank space
                while sReverse[iTmpPos] != " ":
                    # Adding rejected char to variable
                    Throwed = Throwed + sReverse[iTmpPos]
                    # Increment index
                    iTmpPos += 1
                # Deleting rejected chars from reverse temporary line
                sReverse = sReverse[iTmpPos:]
                # Restoring correct course
                sTmpStr = sReverse[::-1]
                # Adding char of new line to the end of temporary line
                sTmpStr = sTmpStr + '\n'
                # Adding split line to variable
                sFinalResult = sFinalResult + sTmpStr
                # Saving to the temporary line inverted rejected chars
                sTmpStr = "" + Throwed[::-1]

        # Adding result of last iteration to final string
        sFinalResult = sFinalResult + sTmpStr
        # Returning variable
        return sFinalResult

    def BasketContent(self, ev):
        print(self.oBasket.Ordered)
        print(self.oBasket.FullPrice)
        # Label który będzie reprezentował graficznie elementy znajdujące się w koszyku
        # Koszyk w tym module znajduje się pod zmienną self.oBasket

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    ex = FirstPanel()
    sys.exit(app.exec_())
