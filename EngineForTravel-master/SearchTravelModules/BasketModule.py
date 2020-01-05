from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap, QFontDatabase
from SearchTravelModules import InfoWindow


class Basket():
    def __init__(self):
        self.Ordered = [] # Koszyk -> Store
        self.Amount = len(self.Ordered) # Liczba elementów w koszyku
        self.FullPrice = 0 # Wartość koszyka

    def Add(self, DictArg, Title):
        SectionPrice = 0 # Całkowita cena za  poszczególne wakajce
        print(DictArg)
        print(Title) # Nazwa/Tytuł
        TmpDict = dict(Name=Title, Transport=DictArg[0]['Transport']['Type'],
                       TransportPrice=DictArg[0]['Transport']['Price'])
        print("Osoby: ")
        if DictArg[1][0]['Adult']['Amount']: # Liczba dorosłych i cena za pobyt
            print("Dorośli: {} Cena: {}".format(DictArg[1][0]['Adult']['Amount'],DictArg[1][0]['Adult']['FullPrice']))
            TmpDict['AdultAmount'] = DictArg[1][0]['Adult']['Amount']
            TmpDict['AdultPrice'] = DictArg[1][0]['Adult']['FullPrice']
            SectionPrice += DictArg[1][0]['Adult']['FullPrice']

        if DictArg[1][1]['Child']['Amount'] : # Liczba dzieci i cena za pobyt
            print("Dzieci: {} Cena: {}".format(DictArg[1][1]['Child']['Amount'],DictArg[1][1]['Child']['FullPrice']))
            TmpDict['ChildAmount'] = DictArg[1][1]['Child']['Amount']
            TmpDict['ChildPrice'] = DictArg[1][1]['Child']['FullPrice']
            SectionPrice += DictArg[1][1]['Child']['FullPrice']

        if DictArg[1][2]['Senior']['Amount']: # Liczba seniorow i cena za pobyt
            print("Seniorzy: {} Cena: {}".format(DictArg[1][2]['Senior']['Amount'],DictArg[1][2]['Senior']['FullPrice']))
            TmpDict['SeniorAmount'] = DictArg[1][2]['Senior']['Amount']
            TmpDict['SeniorPrice'] = DictArg[1][2]['Senior']['FullPrice']
            SectionPrice += DictArg[1][2]['Senior']['FullPrice']

        print("Transport: {} Cena: {}".format(DictArg[0]['Transport']['Type'], DictArg[0]['Transport']['Price'])) # Rodzaj tarnsportu i cena
        SectionPrice += float(DictArg[0]['Transport']['Price'])
        print("Razem: ", SectionPrice)

        self.Ordered.append(TmpDict)

        self.FullPrice += SectionPrice

    def Test(self):
        print("Basked address: ", hex(id(self)))

class AddToBasketWindow(QWidget):
    def __init__(self, Basket, Transport, PerCost, TransCost, OfV_T):
        super().__init__()
        # Setting Fonts
        QFontDatabase.addApplicationFont("Fonts/DukeFill.ttf")
        QFontDatabase.addApplicationFont("Fonts/Focus-Medium.ttf")
        QFontDatabase.addApplicationFont("Fonts/Roboto-ThinItalic.ttf")

        # Setting styles
        self.QLabelStyle = """QLabel{color: #99cc00;}"""
        self.QLineEditStyle = """QLineEdit{color: #99cc00;font-family:DukeFill;font-size:19px; 
                                            background-color: rgba(0,0,0,0); border: 1px solid #383838;}"""
        self.QPushButtonStyle = """QPushButton { color:rgb(132,189,0); background-color: rgba(0, 0, 0, 0); }"""

        # Setting size variable
        screen = QApplication.primaryScreen().grabWindow(0)
        self.size = screen.size()
        self.WindowWidth = self.size.width() * 30 / 100
        self.WindowHeight = self.size.height() * 40 / 100

        # Dynamic variable to set font size
        self.__fFontSize = self.WindowHeight * 0.03

        # Setting photo on background
        Background = QLabel(self)
        BackgroundIMG = QPixmap("../SearchTravelIMG/tlo.png")
        Background.setPixmap(BackgroundIMG)

        # Deleting frames
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.oBasket = Basket
        self.bTransDL = Transport
        self.PersonCost = PerCost
        self.TransportCost = TransCost
        self.Title = OfV_T

        # Drawing UI
        self.initUI()

    def initUI(self):
        # Setting font for whole window
        self.font = QFont()
        self.font.setFamily("DukeFill")
        self.font.setPointSize(self.__fFontSize)

        # Drawing form
        self.MainRect()
        # Drawing button
        self.ButtonExit()
        # Drawing transport section
        self.TransportSelect()
        # Drawing people section
        self.People()
        # Drawing button
        self.SendToBasketButt()

    def MainRect(self):
        rMainRect = QLabel(self)
        rMainRect.setGeometry(self.WindowWidth * 0 / 100, self.WindowHeight * 0 / 100, self.WindowWidth,self.WindowHeight * 50 / 100)
        rMainRect.setStyleSheet("QLabel { background-color : #1c1c1f;}")

    def ButtonExit(self):
        exit = QLabel(self)
        exit.move(self.WindowWidth*92/100,self.WindowHeight*3/100)
        exit.resize(self.WindowWidth * 5 / 100, self.WindowHeight * 3 / 100)
        exit.setStyleSheet("QLabel { background-color : #dc143c;}")
        exit.mousePressEvent = self.exit

    def TransportSelect(self):
        TransLabel = QLabel(self)
        TransLabel.setGeometry(self.WindowWidth*5/100, self.WindowHeight*10/100, self.WindowWidth*40/100, self.WindowHeight*5/100)
        TransLabel.setStyleSheet(self.QLabelStyle)
        TransLabel.setText("Wybierz środek transportu:")
        TransLabel.setFont(self.font)

        self.TransSelect = QComboBox(self)
        if self.bTransDL[0][0]: self.TransSelect.addItem("Autokar")
        if self.bTransDL[0][1]: self.TransSelect.addItem("Pociąg")
        if self.bTransDL[0][2]: self.TransSelect.addItem("Samolot")
        if self.bTransDL[0][3]: self.TransSelect.addItem("Statek")
        self.TransSelect.move(self.WindowWidth*45/100, self.WindowHeight*9/100)

    def People(self):
        # QLabels
        ChildLabel = QLabel(self)
        ChildLabel.setGeometry(self.WindowWidth*5/100, self.WindowHeight*20/100, self.WindowWidth*10/100, self.WindowHeight*5/100)
        ChildLabel.setStyleSheet(self.QLabelStyle)
        ChildLabel.setText("Dzieci: ")
        ChildLabel.setFont(self.font)

        AdultLabel = QLabel(self)
        AdultLabel.setGeometry(self.WindowWidth*5/100, self.WindowHeight*30/100, self.WindowWidth*15/100, self.WindowHeight*5/100)
        AdultLabel.setStyleSheet(self.QLabelStyle)
        AdultLabel.setText("Dorośli: ")
        AdultLabel.setFont(self.font)

        SeniorLabel = QLabel(self)
        SeniorLabel.setGeometry(self.WindowWidth*5/100, self.WindowHeight*40/100, self.WindowWidth*15/100, self.WindowHeight*5/100)
        SeniorLabel.setStyleSheet(self.QLabelStyle)
        SeniorLabel.setText("Seniorzy: ")
        SeniorLabel.setFont(self.font)

        # QLineEdit
        self.ChildLE = QLineEdit(self)
        self.ChildLE.setGeometry(self.WindowWidth*20/100, self.WindowHeight*20/100, self.WindowWidth*10/100, self.WindowHeight*5/100)
        self.ChildLE.setStyleSheet(self.QLineEditStyle)
        self.ChildLE.setFont(self.font)

        self.AdultLE = QLineEdit(self)
        self.AdultLE.setGeometry(self.WindowWidth*20/100, self.WindowHeight*30/100, self.WindowWidth*10/100, self.WindowHeight*5/100)
        self.AdultLE.setStyleSheet(self.QLineEditStyle)
        self.AdultLE.setFont(self.font)

        self.SeniorLE = QLineEdit(self)
        self.SeniorLE.setGeometry(self.WindowWidth*20/100, self.WindowHeight*40/100, self.WindowWidth*10/100, self.WindowHeight*5/100)
        self.SeniorLE.setStyleSheet(self.QLineEditStyle)
        self.SeniorLE.setFont(self.font)

    def SendToBasketButt(self):
        SendButton = QPushButton("Dodaj", self)
        SendButton.setStyleSheet(self.QPushButtonStyle)
        SendButton.setGeometry(self.WindowWidth*80/100, self.WindowHeight*40/100, self.WindowWidth*10/100, self.WindowWidth*5/100)
        SendButton.clicked.connect(self.SendToBasket)

    def SendToBasket(self):
        bError = False
        bErrorPA = False
        iEPA_Counter = 0
        strP_L = ["Adult", "Child", "Senior"]

        PriceDepend = dict(Transport="", Adult=0, Child=0, Senior=0)
        PriceDepend["Transport"] = self.TransSelect.currentText()

        for str in [self.AdultLE.text(), self.ChildLE.text(), self.SeniorLE.text()]:
            if str == "":
                str = 0
            if self.str_isInt(str):
                if str !=0 and self.PersonCost[0][iEPA_Counter] == 0:
                    bErrorPA = True
                iEPA_Counter += 1
                for key in strP_L:
                    PriceDepend[key] = str
                    del strP_L[0]
                    break
            else:
                bError = True

        if bError: self.ShowStatusWindow("Sprawdź poprawność wprowadzonych danych!")
        if bErrorPA: self.ShowStatusWindow("Oferta jest nie dostępna dla podanych osób!")
        else:
            PD_Dict = self.CalculateCosts(PriceDepend)
            self.oBasket.Add(PD_Dict, self.Title)
            self.ShowStatusWindow("Dodano do koszyka.")

    # Function which checking if forwarded string can be converted to int
    def str_isInt(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    def CalculateCosts(self, PriceDepend):
        TransportList = ["Autokar", "Pociąg", "Samolot", "Statek"]
        PriceDetails = []
        Counter = 0

        for TransMode in TransportList:
            if PriceDepend['Transport'] == TransMode:
                Transport = dict(Transport=dict(Type=TransMode, Price=self.TransportCost[0][Counter]))
                PriceDetails.append(Transport)
                break
            Counter += 1

        People = []
        Adult = dict(Adult=dict(Amount=PriceDepend['Adult'], Price=self.PersonCost[0][0],
                                FullPrice=int(PriceDepend['Adult'])*float(self.PersonCost[0][0])))
        Child = dict(Child=dict(Amount=PriceDepend['Child'], Price=self.PersonCost[0][1],
                                FullPrice=int(PriceDepend['Child'])*float(self.PersonCost[0][1])))
        Senior = dict(Senior=dict(Type='Senior', Amount=PriceDepend['Senior'], Price=self.PersonCost[0][2],
                                  FullPrice=int(PriceDepend['Senior'])*float(self.PersonCost[0][2])))
        People.append(Adult)
        People.append(Child)
        People.append(Senior)
        PriceDetails.append(People)
        return PriceDetails

    def exit(self, event):
        self.close()

    def ShowStatusWindow(self, message):
        self.StatusWindow = InfoWindow.StateWindow(message)
        self.StatusWindow.show()