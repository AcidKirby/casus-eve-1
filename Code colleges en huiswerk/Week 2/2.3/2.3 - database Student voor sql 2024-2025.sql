-- phpMyAdmin SQL Dump
-- version 4.7.0
-- 
--
--
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
-- ----------------------------------------------------------
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
-- ----------------------------------------------------------
-- Deze dump bevat de volgende database
-- Student (1 tabel)		30






-- ----------------------------------------------------------------------------------------------------------
-- ----------------------------------------------------------------------------------------------------------
--                                       DATABASE: `student`
-- ----------------------------------------------------------------------------------------------------------
-- ----------------------------------------------------------------------------------------------------------
DROP DATABASE IF EXISTS `student`;
CREATE DATABASE IF NOT EXISTS `student` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `student`;
-- --------------------------------------------------------
--
-- Tabelstructuur voor tabel `student`
--
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `studentnummer` varchar(8) NOT NULL,
  `voornaam` varchar(30) NOT NULL,
  `achternaam` varchar(50) NOT NULL,
  `adres` varchar(50) DEFAULT NULL,
  `woonplaats` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
--
--
INSERT INTO `student` (`studentnummer`, `voornaam`, `achternaam`, `adres`, `woonplaats`) VALUES
('S1000016', 'Sjors', 'van \'t Hart', 'Kampstraat 19', 'Deventer'),
('S1000200', 'Xavi', 'Marijnnissen', 'Schoolstraat 12', 'Zwolle'),
('S1001902', 'Eddie', 'Adelaar', 'Kampstraat 33 ', 'Deventer'),
('S1088553', 'Marnix', 'Koller', 'Havelaan 4', 'Kampen'),
('S2001240', 'Sjors', 'van Dam', 'Muziekweg 14', 'Olst'),
('S2011121', 'Sifan', 'Hassan', 'Kade 241', 'Urk'),
('S2026008', 'Erik', 'Komeens', 'Brinkstraat 2', 'Schalkhaar'),
('S2026708', 'Arda', 'Güler', 'Brinkstraat 2', 'Almere'),
('S2888442', 'Alexandra', 'Schalke', 'Brink 13', 'Breda'),
('S2888443', 'Sebastian', 'Szymański', 'Plein 13', 'Breda'),
('S2888543', 'Dayotchanculle Oswald', 'Upamecano', 'Place 13', 'Castelré'),
('S1888331', 'Sjors', 'Akdiz', 'Dieze 13', 'Zwolle');
--
--
-- Indexen voor tabellen
--
-- Indexen voor tabel `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentnummer`);

COMMIT;