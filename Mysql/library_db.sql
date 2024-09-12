-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 12, 2024 at 01:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_id` int(11) NOT NULL,
  `book_code` varchar(10) NOT NULL,
  `book_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `book_code`, `book_name`) VALUES
(1, 'B001', 'Introduction to the Theory of Computation'),
(2, 'B002', 'Computer Systems: A Programmer\'s Perspective'),
(3, 'B003', 'Operating System Concepts'),
(4, 'B004', 'Database System Concepts'),
(5, 'B005', 'Artificial Intelligence: A Modern Approach'),
(6, 'B006', 'Computer Networking: A Top-Down Approach'),
(7, 'B007', 'Computer Architecture: A Quantitative Approach'),
(8, 'B008', 'Algorithms'),
(9, 'B009', 'Data Structures and Algorithm Analysis in C++'),
(10, 'B010', 'Introduction to Machine Learning'),
(11, 'B011', 'Modern Operating Systems'),
(12, 'B012', 'Compilers: Principles, Techniques, and Tools'),
(13, 'B013', 'Software Engineering: A Practitioner\'s Approach'),
(14, 'B014', 'Computer Vision: Algorithms and Applications'),
(15, 'B015', 'Digital Design and Computer Architecture'),
(16, 'B016', 'Introduction to Quantum Computing'),
(17, 'B017', 'Data Mining: Concepts and Techniques'),
(18, 'B018', 'Computer Graphics: Principles and Practice'),
(19, 'B019', 'Principles of Compiler Design'),
(20, 'B020', 'Computer Organization and Design: The Hardware/Software Interface'),
(21, 'B021', 'Introduction to Computer Science Using Python'),
(22, 'B022', 'Introduction to Information Systems'),
(23, 'B023', 'Computer Science: An Overview'),
(24, 'B024', 'Understanding Machine Learning: From Theory to Algorithms'),
(25, 'B025', 'Computer Vision: A Modern Approach'),
(26, 'B026', 'Design Patterns: Elements of Reusable Object-Oriented Software'),
(27, 'B027', 'Operating Systems: Internals and Design Principles'),
(28, 'B028', 'Computer Security: Principles and Practice'),
(29, 'B029', 'Human-Computer Interaction'),
(30, 'B030', 'Introduction to Cloud Computing');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `student_lib_id` varchar(10) NOT NULL,
  `borrowed_books` text DEFAULT NULL,
  `history` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_id`, `student_name`, `student_lib_id`, `borrowed_books`, `history`) VALUES
(1, 'star', 'star', '[{\"code\": \"B001\", \"borrow_date\": \"2024-09-12\", \"return_date\": \"2024-09-12\"}]', '[{\"code\": \"B001\", \"borrow_date\": \"2024-09-12\", \"return_date\": \"2024-09-12\"}]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`),
  ADD UNIQUE KEY `book_code` (`book_code`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `student_lib_id` (`student_lib_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
