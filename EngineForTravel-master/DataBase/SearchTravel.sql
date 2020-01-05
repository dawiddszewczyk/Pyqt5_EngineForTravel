-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Additional`
--

LOCK TABLES `Additional` WRITE;
/*!40000 ALTER TABLE `Additional` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contact`
--

LOCK TABLES `Contact` WRITE;
/*!40000 ALTER TABLE `Contact` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Costs`
--

LOCK TABLES `Costs` WRITE;
/*!40000 ALTER TABLE `Costs` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Offers`
--

LOCK TABLES `Offers` WRITE;
/*!40000 ALTER TABLE `Offers` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OffersDetails`
--

LOCK TABLES `OffersDetails` WRITE;
/*!40000 ALTER TABLE `OffersDetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `OffersDetails` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transport`
--

LOCK TABLES `Transport` WRITE;
/*!40000 ALTER TABLE `Transport` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transport` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UsersDetails`
--

LOCK TABLES `UsersDetails` WRITE;
/*!40000 ALTER TABLE `UsersDetails` DISABLE KEYS */;
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

-- Dump completed on 2018-05-29 17:17:03
