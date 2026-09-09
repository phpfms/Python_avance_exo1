-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mer. 09 sep. 2026 à 11:18
-- Version du serveur : 11.7.1-MariaDB
-- Version de PHP : 8.5.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ecole`
--

-- --------------------------------------------------------

--
-- Structure de la table `address`
--

CREATE TABLE `address` (
  `id_address` int(11) NOT NULL,
  `street` varchar(80) NOT NULL,
  `city` varchar(50) NOT NULL,
  `postal_code` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `address`
--

INSERT INTO `address` (`id_address`, `street`, `city`, `postal_code`) VALUES
(1, '12 rue des Pinsons', 'Castanet', '31320'),
(2, '43 avenue Jean Zay', 'Toulouse', '31200'),
(3, '7 impasse des Coteaux', 'Cornebarrieu', '31150'),
(4, '123 rue de loin', 'tatouine', '99999'),
(6, '123 rue de loin', 'tatouine', '99999'),
(7, '123 rue de loin', 'tatouine', '99999'),
(8, '123 rue de loin', 'tatouine', '99999'),
(9, '123 rue de loin', 'tatouine', '99999'),
(10, '10 rue de Paris', 'Toulouse', '31000'),
(11, '10 rue de Paris', 'Toulouse', '31000'),
(12, '20 rue de Bordeaux', 'Bordeaux', '33000'),
(14, '10 rue de Paris', 'Toulouse', '31000'),
(15, '10 rue de Paris', 'Toulouse', '31000'),
(16, '20 rue de Bordeaux', 'Bordeaux', '33000'),
(18, '10 rue de Paris', 'Toulouse', '31000'),
(19, '10 rue de Paris', 'Toulouse', '31000'),
(20, '20 rue de Bordeaux', 'Bordeaux', '33000');

-- --------------------------------------------------------

--
-- Structure de la table `course`
--

CREATE TABLE `course` (
  `id_course` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `id_teacher` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `course`
--

INSERT INTO `course` (`id_course`, `name`, `start_date`, `end_date`, `id_teacher`) VALUES
(1, 'Français', '2024-01-29', '2024-02-16', 1),
(2, 'Histoire', '2024-02-05', '2024-02-16', 2),
(3, 'Géographie', '2024-02-05', '2024-02-16', 2),
(4, 'Mathématiques', '2024-02-12', '2024-03-08', 3),
(5, 'Physique', '2024-02-19', '2024-03-08', 4),
(6, 'Chimie', '2024-02-26', '2024-03-15', 4),
(7, 'Anglais', '2024-02-12', '2024-02-24', 5),
(8, 'Sport', '2024-03-04', '2024-03-15', 6),
(9, 'Mathématiques', '2024-02-12', '2024-03-08', 15),
(10, 'Mathématiques', '2024-02-12', '2024-03-08', 16),
(11, 'Physique', '2024-02-19', '2024-03-15', 17);

-- --------------------------------------------------------

--
-- Structure de la table `person`
--

CREATE TABLE `person` (
  `id_person` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `age` tinyint(4) NOT NULL,
  `id_address` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`id_person`, `first_name`, `last_name`, `age`, `id_address`) VALUES
(1, 'Paul', 'Dubois', 12, 1),
(2, 'Valérie', 'Dumont', 13, 2),
(3, 'Louis', 'Berthot', 11, 3),
(4, 'Victor', 'Hugo', 23, NULL),
(5, 'Jules', 'Michelet', 32, NULL),
(6, 'Sophie', 'Germain', 25, NULL),
(7, 'Marie', 'Curie', 31, NULL),
(8, 'William', 'Shakespeare', 34, NULL),
(9, 'Michel', 'Platini', 42, NULL),
(10, 'Paul', 'Dubois', 12, NULL),
(11, 'Paul', 'Dubois', 12, NULL),
(12, 'Jean', 'Dupont', 25, NULL),
(14, 'Paul', 'Dubois', 12, NULL),
(15, 'Paul', 'Dubois', 12, NULL),
(16, 'Jean', 'Dupont', 25, NULL),
(18, 'Victor', 'Hugo', 23, NULL),
(19, 'Victor', 'Hugo', 23, NULL),
(20, 'Victor', 'Hugo', 23, NULL),
(21, 'Victor', 'Hugo', 23, NULL),
(22, 'Victor', 'Hugo', 23, NULL),
(23, 'Victor', 'Hugo', 23, NULL),
(24, 'Victor', 'Hugo', 23, NULL),
(25, 'Victor', 'Hugo', 23, NULL),
(26, 'Victor', 'Hugo', 23, NULL),
(27, 'Victor', 'Hugo', 23, NULL),
(28, 'Victor', 'Hugo', 23, NULL),
(29, 'Victor', 'Hugo', 23, NULL),
(30, 'Paul', 'Dubois', 12, NULL),
(31, 'Paul', 'Dubois', 12, NULL),
(32, 'Jean', 'Dupont', 25, NULL),
(34, 'Paul', 'Dubois', 12, NULL),
(35, 'Paul', 'Dubois', 12, NULL),
(36, 'Jean', 'Dupont', 25, NULL),
(38, 'Paul', 'Dubois', 12, NULL),
(39, 'Paul', 'Dubois', 12, NULL),
(40, 'Paul', 'Dubois', 12, NULL),
(42, 'Paul', 'Dubois', 12, NULL),
(43, 'Paul', 'Dubois', 12, NULL),
(44, 'Jean', 'Dupont', 25, NULL),
(46, 'Paul', 'Dubois', 12, NULL),
(47, 'Paul', 'Dubois', 12, NULL),
(48, 'Paul', 'Dubois', 12, NULL),
(49, 'Paul', 'Dubois', 12, NULL),
(50, 'Paul', 'Dubois', 12, NULL),
(51, 'Paul', 'Dubois', 12, NULL),
(52, 'Paul', 'Dubois', 12, NULL),
(53, 'Paul', 'Dubois', 12, NULL),
(54, 'Paul', 'Dubois', 12, NULL),
(55, 'Paul', 'Dubois', 12, NULL),
(56, 'Jean', 'Dupont', 15, NULL),
(57, 'Paul', 'Dubois', 12, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `student`
--

CREATE TABLE `student` (
  `student_nbr` int(11) NOT NULL,
  `id_person` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `student`
--

INSERT INTO `student` (`student_nbr`, `id_person`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 49),
(5, 54),
(6, 55),
(7, 56);

-- --------------------------------------------------------

--
-- Structure de la table `takes`
--

CREATE TABLE `takes` (
  `student_nbr` int(11) NOT NULL,
  `id_course` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `takes`
--

INSERT INTO `takes` (`student_nbr`, `id_course`) VALUES
(2, 1),
(2, 2),
(1, 3),
(3, 3),
(3, 4),
(1, 5),
(3, 5),
(2, 6),
(1, 7),
(3, 8);

-- --------------------------------------------------------

--
-- Structure de la table `teacher`
--

CREATE TABLE `teacher` (
  `id_teacher` int(11) NOT NULL,
  `hiring_date` date NOT NULL,
  `id_person` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `teacher`
--

INSERT INTO `teacher` (`id_teacher`, `hiring_date`, `id_person`) VALUES
(1, '2023-09-04', 4),
(2, '2023-09-04', 5),
(3, '2023-09-04', 6),
(4, '2023-09-04', 7),
(5, '2023-09-04', 8),
(6, '2023-09-04', 9),
(7, '2023-09-04', 18),
(8, '2023-09-04', 19),
(9, '2023-09-04', 20),
(11, '2023-09-04', 22),
(12, '2023-09-04', 23),
(13, '2024-09-01', 24),
(15, '2023-09-04', 26),
(16, '2023-09-04', 27),
(17, '2023-09-04', 28),
(18, '2023-09-04', 29);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `address`
--
ALTER TABLE `address`
  ADD PRIMARY KEY (`id_address`);

--
-- Index pour la table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id_course`),
  ADD KEY `id_teacher` (`id_teacher`);

--
-- Index pour la table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id_person`),
  ADD UNIQUE KEY `id_address` (`id_address`);

--
-- Index pour la table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_nbr`),
  ADD UNIQUE KEY `id_person` (`id_person`);

--
-- Index pour la table `takes`
--
ALTER TABLE `takes`
  ADD PRIMARY KEY (`student_nbr`,`id_course`),
  ADD KEY `id_course` (`id_course`);

--
-- Index pour la table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`id_teacher`),
  ADD UNIQUE KEY `id_person` (`id_person`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `address`
--
ALTER TABLE `address`
  MODIFY `id_address` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `course`
--
ALTER TABLE `course`
  MODIFY `id_course` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `person`
--
ALTER TABLE `person`
  MODIFY `id_person` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT pour la table `student`
--
ALTER TABLE `student`
  MODIFY `student_nbr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `id_teacher` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`id_teacher`) REFERENCES `teacher` (`id_teacher`);

--
-- Contraintes pour la table `person`
--
ALTER TABLE `person`
  ADD CONSTRAINT `person_ibfk_1` FOREIGN KEY (`id_address`) REFERENCES `address` (`id_address`);

--
-- Contraintes pour la table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `takes`
--
ALTER TABLE `takes`
  ADD CONSTRAINT `takes_ibfk_1` FOREIGN KEY (`student_nbr`) REFERENCES `student` (`student_nbr`),
  ADD CONSTRAINT `takes_ibfk_2` FOREIGN KEY (`id_course`) REFERENCES `course` (`id_course`);

--
-- Contraintes pour la table `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
