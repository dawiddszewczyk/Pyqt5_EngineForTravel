-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: SearchTravel
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Additional`
--

DROP TABLE IF EXISTS `Additional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Additional` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) DEFAULT NULL,
  `WWW` varchar(200) DEFAULT NULL,
  `FB` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `Additional_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Additional`
--

LOCK TABLES `Additional` WRITE;
/*!40000 ALTER TABLE `Additional` DISABLE KEYS */;
INSERT INTO `Additional` VALUES (1,1,'BRAK','BRAK'),(2,2,'www.swedenholiday.com','www.facebook.com/holidayinsweden'),(3,3,'wakacjazagranica.pl','www.facebok.com/wakacjezagranica');
/*!40000 ALTER TABLE `Additional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contact`
--

DROP TABLE IF EXISTS `Contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Contact` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) DEFAULT NULL,
  `Telephone` int(11) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Address` text,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `Contact_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contact`
--

LOCK TABLES `Contact` WRITE;
/*!40000 ALTER TABLE `Contact` DISABLE KEYS */;
INSERT INTO `Contact` VALUES (1,1,2147483647,'BRAK','39-1939 Nigerland ul. gen.Makumby 14'),(2,2,2147483647,'holiday@sweden.sw',''),(3,3,2147483647,'wakacjezagranica@poland.pl','Warszawa 00-001 ul. Powstańców 423');
/*!40000 ALTER TABLE `Contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Costs`
--

DROP TABLE IF EXISTS `Costs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Costs` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) NOT NULL,
  `Adult` decimal(20,2) DEFAULT NULL,
  `Child` decimal(20,2) DEFAULT NULL,
  `Senior` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `Costs_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Costs`
--

LOCK TABLES `Costs` WRITE;
/*!40000 ALTER TABLE `Costs` DISABLE KEYS */;
INSERT INTO `Costs` VALUES (1,1,15.20,0.50,0.00),(2,2,74.10,40.00,35.50),(3,3,0.00,20.50,0.00);
/*!40000 ALTER TABLE `Costs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Offers`
--

DROP TABLE IF EXISTS `Offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Offers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` text,
  `ShortDescription` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Offers`
--

LOCK TABLES `Offers` WRITE;
/*!40000 ALTER TABLE `Offers` DISABLE KEYS */;
INSERT INTO `Offers` VALUES (1,'Wymarzone wakacje w Nigerii','Marzyłeś o tym aby wziąć udział w powstaniu przeciwko białemu panu? Chcesz poznać prawdziwą biedę? W takim razie zapraszamy!'),(2,'Wakacje w Sundsvall','Spędź razem ze swoją drugą połówką wakacje w przepięknym, szwedzkim miasteczku portowym Sundsvall.'),(3,'Obóz letni we Włoszech','Zapraszamy na młodzieżowy obóz letni we Włoszech. W planach podróży między innymi wizyta u Papieża!');
/*!40000 ALTER TABLE `Offers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OffersDetails`
--

DROP TABLE IF EXISTS `OffersDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OffersDetails` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) NOT NULL,
  `Name` text,
  `Description` text,
  `Country` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `OffersDetails_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OffersDetails`
--

LOCK TABLES `OffersDetails` WRITE;
/*!40000 ALTER TABLE `OffersDetails` DISABLE KEYS */;
INSERT INTO `OffersDetails` VALUES (1,1,'Wojna domowa w Nigerii','Nie masz planów na wakacje? Oburza cię kapitalizm i zwierzchnictwo klas wyższych? Czujesz potrzebę wzięcia udziału w rewolucji? W takim razie świetnie trafiłeś! Wojna w Nigerii będzie dla ciebie idealnym wydarzenia na zaspokojenie swoich potrzeb. Walcz w szeregach Legii Murzyńskiej, pokonuj białego ciemiężyciela, zabierz mu ziemię! Oferujemy darmowy transport dorgą morska. Poszukujemy w szczególności dzieci, jako do prodzukcji domowych-bomb. Dzięki nam masz możliwość wcielenia się w różne kalsy np: szturmowca, zamachowca, zabójcę etc. Wszystko to tylko w Nigerii. Viva la Revolution!','Nigeria'),(2,2,'Szwecja!','Wakacje dla dwojga w malowniczej Szwecjii. Oferujemy nocleg w przepięknym miasteczku Sundsvall, oraz wycieczki po całej Szwecji jak i Norwegii. Pozwól aby skandynawski klimat całkowicie Tobą zawładnął. Nie przegam naszej oferty. Zapraszamy!','Szwecja'),(3,3,'Dare all\'Imperatore','Wybierz się na wspaniałą podróż do Włoch, do kraju na którego ziemiach w starożytności rozkwitło jedno z najpotężniejszych mocarstw tamtej epoki. Złóż wizytę Papieżowi, podziwiaj Watykan, spotkaj się z legendarną Gwardią Szwajcarską! Poznaj historię starożytnego Rzymu, zagłęb się w tajniki cesarstwa, weź udział w rekonstrukcji walk legionistów.\nCivis Romanus sum.','Włochy');
/*!40000 ALTER TABLE `OffersDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pictures`
--

DROP TABLE IF EXISTS `Pictures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pictures` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) NOT NULL,
  `Picture` text,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `Pictures_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pictures`
--

LOCK TABLES `Pictures` WRITE;
/*!40000 ALTER TABLE `Pictures` DISABLE KEYS */;
INSERT INTO `Pictures` VALUES (1,1,'Niger/Niger1'),(2,1,'Niger/Niger2'),(3,1,'Niger/Niger3'),(4,2,'Sweden/Sweden1'),(5,2,'Sweden/Sweden2'),(6,2,'Sweden/Sweden3'),(7,3,'Italia/Italia1'),(8,3,'Italia/Italia2'),(9,3,'Italia/Italia3');
/*!40000 ALTER TABLE `Pictures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transport`
--

DROP TABLE IF EXISTS `Transport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transport` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) NOT NULL,
  `Bus` tinyint(1) DEFAULT NULL,
  `Train` tinyint(1) DEFAULT NULL,
  `Plane` tinyint(1) DEFAULT NULL,
  `Ship` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `Transport_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transport`
--

LOCK TABLES `Transport` WRITE;
/*!40000 ALTER TABLE `Transport` DISABLE KEYS */;
INSERT INTO `Transport` VALUES (1,1,0,0,0,1),(2,2,0,0,1,1),(3,3,1,1,1,1);
/*!40000 ALTER TABLE `Transport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TransportCost`
--

DROP TABLE IF EXISTS `TransportCost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TransportCost` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `OfferID` int(11) NOT NULL,
  `BusCost` decimal(20,2) DEFAULT NULL,
  `TrainCost` decimal(20,2) DEFAULT NULL,
  `PlaneCost` decimal(20,2) DEFAULT NULL,
  `ShipCost` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `OfferID` (`OfferID`),
  CONSTRAINT `TransportCost_ibfk_1` FOREIGN KEY (`OfferID`) REFERENCES `Offers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransportCost`
--

LOCK TABLES `TransportCost` WRITE;
/*!40000 ALTER TABLE `TransportCost` DISABLE KEYS */;
INSERT INTO `TransportCost` VALUES (1,1,0.00,0.00,0.00,185.50),(2,2,0.00,0.00,325.00,185.50),(3,3,50.00,64.50,825.00,355.50);
/*!40000 ALTER TABLE `TransportCost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Login` varchar(30) NOT NULL,
  `Password` varchar(128) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'','LennyHere'),(2,'Izabela','Dejw'),(3,'Edward','edw'),(4,'Jan','JanK');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UsersDetails`
--

DROP TABLE IF EXISTS `UsersDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UsersDetails` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) NOT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(80) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL,
  `Avatar` text,
  PRIMARY KEY (`ID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `UsersDetails_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UsersDetails`
--

LOCK TABLES `UsersDetails` WRITE;
/*!40000 ALTER TABLE `UsersDetails` DISABLE KEYS */;
INSERT INTO `UsersDetails` VALUES (1,1,'Kristine','Frosteh','k.frostech@gmail.com','/img/kristine/av.png'),(2,2,'Izabela','Rurowska','izabela.takeme@gmail.com','/img/izabela/iz.png'),(3,3,'Edward','Koszyński','edward.koszynski@industry.com','/img/edward/edw.png'),(4,3,'Jan','Kowalski','jkowalski@gmail.com','/img/jan/jan.png');
/*!40000 ALTER TABLE `UsersDetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-21 12:11:02
