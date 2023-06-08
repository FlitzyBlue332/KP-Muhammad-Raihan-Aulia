-- MariaDB dump 10.19  Distrib 10.10.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: lokerdb
-- ------------------------------------------------------
-- Server version	10.10.2-MariaDB

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
-- Table structure for table `loker`
--

DROP TABLE IF EXISTS `loker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loker` (
  `lokerid` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) DEFAULT NULL,
  `filled` tinyint(1) NOT NULL DEFAULT 0,
  `password` varchar(255) DEFAULT NULL,
  `userNIK` varchar(255) DEFAULT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `userPhone` varchar(255) DEFAULT NULL,
  `userMail` varchar(255) DEFAULT NULL,
  `dateSimpan` date DEFAULT NULL,
  PRIMARY KEY (`lokerid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loker`
--

LOCK TABLES `loker` WRITE;
/*!40000 ALTER TABLE `loker` DISABLE KEYS */;
INSERT INTO `loker` VALUES
(1,'big',1,'asadayo','121','uwu','089','sa@mail.com','2020-06-06'),
(2,'big',0,NULL,NULL,NULL,NULL,NULL,NULL),
(3,'big',0,NULL,NULL,NULL,NULL,NULL,NULL),
(4,'big',0,NULL,NULL,NULL,NULL,NULL,NULL),
(5,'big',0,NULL,NULL,NULL,NULL,NULL,NULL),
(6,'small',0,NULL,NULL,NULL,NULL,NULL,NULL),
(7,'small',0,NULL,NULL,NULL,NULL,NULL,NULL),
(8,'small',0,NULL,NULL,NULL,NULL,NULL,NULL),
(9,'small',1,'password','28193812','minut','81298312','mail@mail.com','2020-06-08'),
(10,'small',0,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `loker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaksi`
--

DROP TABLE IF EXISTS `transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaksi` (
  `idTransaksi` int(11) NOT NULL AUTO_INCREMENT,
  `lokerid` int(11) NOT NULL,
  `dateTransaksi` date DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  PRIMARY KEY (`idTransaksi`),
  KEY `lokerid` (`lokerid`),
  CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`lokerid`) REFERENCES `loker` (`lokerid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaksi`
--

LOCK TABLES `transaksi` WRITE;
/*!40000 ALTER TABLE `transaksi` DISABLE KEYS */;
INSERT INTO `transaksi` VALUES
(1,2,'2023-06-08',0),
(2,10,'2023-06-08',19710000),
(3,2,'2023-06-08',0),
(4,6,'2023-06-08',0),
(5,2,'2023-06-08',0);
/*!40000 ALTER TABLE `transaksi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-08 15:42:06
