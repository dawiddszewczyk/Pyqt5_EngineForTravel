import mysql.connector
from ftplib import FTP
import os

databaseConnection = {
    'user': 'NoteUser',
    'password': 'Note',
    'host': '192.168.1.15',
    'database': 'SearchTravel'
}


class Data():
    def __init__(self):
        """To implement this class in another module use class instance
           Ex:
           from __YOUR__HEAD__DIRECTORY__ import DatabaseQuery
           clD = DatabaseQuery.Data()
           clD.__HERE__PASTE__FUNCTIONS__FROM_CLASS
        """
        # Global variables to store data from OfferDetails
        self.MainDetail = None
        self.Transport = None
        self.Costs = None
        self.Contact = None
        self.Additional = None
        self.TransportCosts = None
        # End of OfferDetails variables

        # Global variables to store data from OfferView
        self.ViewInformation = None
        self.PicturesPath = None
        # End of OfferView variables

        # Global variable to store data from Filters
        self.FilteredResult = None
        # End of Filters variable

    def OfferDeatails(self, OfferID):
        # Connecting section -> Connecting with database
        ConnectDB = mysql.connector.connect(user=databaseConnection['user'],password=databaseConnection['password'],
                                            host=databaseConnection['host'],database=databaseConnection['database'])
        # Creating cursor to executing query(ies)
        DataBaseOperate = ConnectDB.cursor()
        # End of connecting section

        # Query section
        sMainDetail = "SELECT Name,Description,Country FROM OffersDetails WHERE OfferID={0}".format(OfferID)
        sTransport = "SELECT Bus,Train,Plane,Ship FROM Transport WHERE OfferID={0}".format(OfferID)
        sCosts = "SELECT Adult,Child,Senior FROM Costs WHERE OfferID={0}".format(OfferID)
        sContact = "SELECT Telephone,Email,Address FROM Contact WHERE OfferID={0}".format(OfferID)
        sAdditional = "SELECT WWW,FB FROM Additional WHERE OfferID={0}".format(OfferID)
        sTransportCosts = "SELECT BusCost,TrainCost,PlaneCost,ShipCost FROM TransportCost WHERE OfferID={0}".format(OfferID)
        # End of query section

        # Executing query section -> Execute query and save returned tuples to  list
        DataBaseOperate.execute(sMainDetail)
        self.MainDetail = DataBaseOperate.fetchall()         # Store name and description about place and country where this place is
        DataBaseOperate.execute(sTransport)                  # Name -> [0]; Description -> [1]; Country -> [2]
        self.Transport = DataBaseOperate.fetchall()          # Store data about availability of  bus, train, plane or ship
        DataBaseOperate.execute(sCosts)                      # Bus -> [0]; Train -> [1]; Plane -> [2]; Ship -> [3]
        self.Costs = DataBaseOperate.fetchall()              # Store prices for adult, child and senior
        DataBaseOperate.execute(sContact)                    # Adult -> [0]; Child -> [1]; Senior -> [2]
        self.Contact = DataBaseOperate.fetchall()            # Store telephone number,Email address and company address
        DataBaseOperate.execute(sAdditional)                 #  Telephone -> [0]; Email -> [1]; Address -> [2]
        self.Additional = DataBaseOperate.fetchall()         # Store WWW and FB addresses
                                                             # WWW -> [0}; FB -> [1]
        DataBaseOperate.execute(sTransportCosts)             # Store costs of specific means of travel
        self.TransportCosts = DataBaseOperate.fetchall()     # Bus -> [0]; Train -> [1]; Plane -> [2]; Ship -> [3]
        # End of executing query section

        # Close connecting section
        ConnectDB.close()
        # End of close connecting section

    def OfferView(self):
        # Connecting section -> Connecting with database
        ConnectDB = mysql.connector.connect(user=databaseConnection['user'], password=databaseConnection['password'],
                                            host=databaseConnection['host'], database=databaseConnection['database'])
        # Creating cursor to executing query(ies)
        self.DataBaseOperate = ConnectDB.cursor()
        # End of connecting section

        # Query section
        sViewInformation = "SELECT ID,Name,ShortDescription FROM Offers"
        # End of query section

        # Executing query section -> Execute query and save returned tuples to  list
        self.DataBaseOperate.execute(sViewInformation)
        self.ViewInformation = self.DataBaseOperate.fetchall()        # Store offer's ID, name and short description
        # End of executing query section                         # ID -> [n][0]; Name -> [n][1]; ShortDescription -> [n][2]

        # Close connecting section
        ConnectDB.close()
        # End of close connecting section

    def DownloadPictures(self):
        # Connecting section -> Connecting with database
        ConnectDB = mysql.connector.connect(user=databaseConnection['user'], password=databaseConnection['password'],
                                            host=databaseConnection['host'], database=databaseConnection['database'])
        # Creating cursor to executing query(ies)
        DataBaseOperate = ConnectDB.cursor()
        # End of connecting section

        # Query section
        sPicturesPath = "SELECT ID,OfferID,Picture FROM Pictures"
        # End of query section

        # Executing query section -> Execute query and save returned tuples to  list
        DataBaseOperate.execute(sPicturesPath)
        self.PicturesPath = DataBaseOperate.fetchall()  # Store path to pictures for FTP module
        # End of executing query section                # ID -> [n][0]; OfferID -> [n][1]; PicturePath(Picture) -> [n][2]

        # Close connecting section
        ConnectDB.close()
        # End of close connecting section

        # Connecting FTP section -> Connecting with FTP server and login
        ConnectFTP = FTP(databaseConnection['host'])
        ConnectFTP.login("forker", "FTPLove@@")
        # End of connecting section

        # Downloading pictures section
        for n in range(len(self.PicturesPath)):
            # Splitting PicturesPath string to single string and saving them to sTempPath list
            sTempPath = [sX for sX in self.PicturesPath[n][2].split('/') if sX]
            # Checking if catalog for pictures exist
            if not os.path.exists("../OfferIMG/{0}".format(sTempPath[0])):
                os.makedirs("../OfferIMG/{0}".format(sTempPath[0]))
            # Creating and open local, binary file in write mode
            LocalFile = open("../OfferIMG/{0}".format(self.PicturesPath[n][2]), 'wb')
            # Downloading and saving file from FTP server to local file on client disk
            ConnectFTP.retrbinary('RETR %s' % self.PicturesPath[n][2], LocalFile.write)
            # Close local file
            LocalFile.close()
        # End of downloading picture section

        # Close FTP connection section
        ConnectFTP.quit()
        # End of close connection section

    def Filters(self, DictArgue):
        """
        DictArgue
        "Country": -> Store country name as string
        "PriceSort": -> Store type of sorting as string
        "Transport": -> Store available transport as bool => Bus Train Plane Ship

        """

        # Variable which store the basic query
        BaseQuery = """SELECT Offers.ID, Offers.Name, ShortDescription 
                        FROM Offers, OffersDetails, Costs, Transport 
                        WHERE OffersDetails.OfferID = Offers.ID 
                        AND Offers.ID=Costs.OfferID 
                        AND Offers.ID=Transport.OfferID"""

        TransportAdd = ""

        # Checking if user choosed any country
        if DictArgue['Country']:
            CountryAdd = " AND Country = '{0}'".format(DictArgue['Country'])
        else:
            CountryAdd = ""

        # Checking user price preferences
        if DictArgue['PriceSort']:
            sPricePerson = DictArgue['PriceSort'].split()[0]    # Store type of person: Child, Adult or Senior
            sPriceSort = DictArgue['PriceSort'].split()[1]      # Store type of sorting: decreasing or increasing
            if sPriceSort == "MAX":
                PriceAdd = " ORDER BY({0}) DESC".format(sPricePerson)
            elif sPriceSort == "MIN":
                PriceAdd = " ORDER BY({0}) ASC".format(sPricePerson)

            BaseQuery = BaseQuery.replace("ShortDescription ", "ShortDescription, {0}".format(sPricePerson))
        else:
            PriceAdd = ""

        # Checking available transport
        if DictArgue['Transport'][0]:
            TransportAdd = TransportAdd + " AND Bus=1"
        if DictArgue['Transport'][1]:
            TransportAdd = TransportAdd + " AND Train=1"
        if DictArgue['Transport'][2]:
            TransportAdd = TransportAdd + " AND Plane=1"
        if DictArgue['Transport'][3]:
            TransportAdd = TransportAdd + " AND Ship=1"

        # Query section -> Creating query
        FilterQuery = BaseQuery + CountryAdd + TransportAdd + PriceAdd
        # End of query section

        # Connecting section -> Connecting with database
        ConnectDB = mysql.connector.connect(user=databaseConnection['user'], password=databaseConnection['password'],
                                            host=databaseConnection['host'], database=databaseConnection['database'])
        # Creating cursor to executing query(ies)
        DataBaseOperate = ConnectDB.cursor()
        # End of connecting section

        # Executing query section -> Execute query and save returned tuples to  list
        DataBaseOperate.execute(FilterQuery)
        self.FilteredResult = DataBaseOperate.fetchall()    # Store filtered offers
        # End of executing query section                    # ID -> [n][0]; Name -> [n][1]; ShortDescription -> [n][2];
                                                                                          # Price for person -> [n][3]

        # Close connecting section
        ConnectDB.close()
        # End of close connecting section
