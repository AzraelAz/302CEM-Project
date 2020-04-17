-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2020 at 08:58 AM
-- Server version: 10.1.39-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `logistic_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `customerlist`
--

CREATE TABLE `customerlist` (
  `customerNo` varchar(3) NOT NULL,
  `firstName` text NOT NULL,
  `lastName` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customerlist`
--

INSERT INTO `customerlist` (`customerNo`, `firstName`, `lastName`) VALUES
('001', 'Cherry', 'Lam'),
('002', 'Sam', 'Wong');

-- --------------------------------------------------------

--
-- Table structure for table `loginlist`
--

CREATE TABLE `loginlist` (
  `adminID` varchar(4) NOT NULL,
  `adminPWD` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loginlist`
--

INSERT INTO `loginlist` (`adminID`, `adminPWD`) VALUES
('0001', '0001'),
('0002', '0002');

-- --------------------------------------------------------

--
-- Table structure for table `orderlist`
--

CREATE TABLE `orderlist` (
  `orderNo` int(20) NOT NULL,
  `S_FirstName` varchar(11) NOT NULL,
  `S_LastName` varchar(20) NOT NULL,
  `S_Address` varchar(20) NOT NULL,
  `S_City` varchar(20) NOT NULL,
  `S_Country` varchar(20) NOT NULL,
  `R_FirstName` varchar(20) NOT NULL,
  `R_LastName` varchar(20) NOT NULL,
  `R_Address` varchar(20) NOT NULL,
  `R_City` varchar(20) NOT NULL,
  `R_Country` varchar(20) NOT NULL,
  `ProductName` varchar(20) NOT NULL,
  `OrderQun` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderlist`
--

INSERT INTO `orderlist` (`orderNo`, `S_FirstName`, `S_LastName`, `S_Address`, `S_City`, `S_Country`, `R_FirstName`, `R_LastName`, `R_Address`, `R_City`, `R_Country`, `ProductName`, `OrderQun`) VALUES
(1, 'Tom', 'Lam', 'City street', 'Hong Kong', 'Hong Kong', 'Cherry', 'Lam', 'Hong Kong Street', 'Hong Kong', 'Hong Kong', 'food', '2'),
(2, 'Cherry', 'Chan', 'Lok Hong Road', 'Hong Kong', 'Hong Kong', 'Sam', 'Leung', 'On Fei Road', 'Hong Kong', 'Hong Kong', 'Other', '1'),
(5, 'Tom', 'Lam', 'City Road', 'Hong Kong', 'Hong Kong', 'Cherry', 'Lam', 'Wong Street', 'Hong Kong', 'Hong Kong', 'Food', '9'),
(6, 'Terry', 'Lam', '123 Street', 'Hong Kong', 'Hong Kong', 'Candy', 'Lam', '234 Street', 'Hong Kong', 'Hong Kong', 'HealthCare', '3'),
(7, 'Terry', 'Lam', '123 Street', 'Hong Kong', 'Hong Kong', 'Candy', 'Lam', '234 Street', 'Hong Kong', 'Hong Kong', 'Electronic', '10'),
(8, 'Terry', 'Wong', '123 Street', 'Hong Kong', 'Hong Kong', 'Candy', 'Lam', '234 Street', 'Hong Kong', 'Hong Kong', 'SportsEqu', '4'),
(10, 'Tom', 'Leung', 'TY Street', 'Hong Kong', 'Hong Kong', 'LiLi', 'Li', 'FW Walk', 'Hong Kong', 'Hong Kong', 'Electronic', '2'),
(11, 'Tom', 'Leung', 'T Y Street', 'Hong Kong', 'Hong Hong ', 'LiLi', 'Li', 'FW Road', 'Hong Kong', 'Hong Kong ', 'Electronic', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orderlist`
--
ALTER TABLE `orderlist`
  ADD PRIMARY KEY (`orderNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orderlist`
--
ALTER TABLE `orderlist`
  MODIFY `orderNo` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
