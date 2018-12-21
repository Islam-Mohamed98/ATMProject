-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2018 at 09:43 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `info`
--

-- --------------------------------------------------------

--
-- Table structure for table `atm`
--

CREATE TABLE `atm` (
  `id` int(11) NOT NULL,
  `balance` int(11) NOT NULL,
  `200` int(11) NOT NULL,
  `100` int(11) NOT NULL,
  `50` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `atm`
--

INSERT INTO `atm` (`id`, `balance`, `200`, `100`, `50`) VALUES
(1, 950, 2, 3, 5);

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `ID` int(4) NOT NULL,
  `PIN` int(4) NOT NULL,
  `balance` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`ID`, `PIN`, `balance`) VALUES
(1234, 1234, 87900),
(2222, 2222, 6700);

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `Num` int(11) NOT NULL,
  `ID` int(4) NOT NULL,
  `Date1` varchar(255) NOT NULL,
  `Day1` int(2) NOT NULL,
  `time1` varchar(255) NOT NULL,
  `operation` varchar(255) NOT NULL,
  `1st` int(1) NOT NULL,
  `totalwithdraw` int(11) NOT NULL,
  `totaldepposite` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`Num`, `ID`, `Date1`, `Day1`, `time1`, `operation`, `1st`, `totalwithdraw`, `totaldepposite`) VALUES
(82, 1234, 'Sat Dec 22 18:34:53 2018', 22, '18:34:53', 'withdraw - 2000', 1, 2000, 0),
(83, 1234, 'Sat Dec 22 18:35:00 2018', 22, '18:35:00', 'depposite + 300', 0, 2000, 300);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `atm`
--
ALTER TABLE `atm`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`Num`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `Num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
