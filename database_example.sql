-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 20, 2026 at 08:23 AM
-- Server version: 8.4.3
-- PHP Version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `absensikaryawan`
--

-- --------------------------------------------------------

--
-- Table structure for table `absensi`
--

CREATE TABLE `absensi` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `tanggal` date NOT NULL,
  `jam_masuk` time DEFAULT NULL,
  `jam_pulang` time DEFAULT NULL,
  `status` enum('Hadir') DEFAULT 'Hadir',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status_validasi` enum('pending','approved','rejected') DEFAULT 'pending',
  `catatan_foreman` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `absensi`
--

INSERT INTO `absensi` (`id`, `user_id`, `tanggal`, `jam_masuk`, `jam_pulang`, `status`, `created_at`, `status_validasi`, `catatan_foreman`) VALUES
(3, 4, '2026-01-06', '13:17:52', '13:17:54', 'Hadir', '2026-01-06 06:17:52', 'pending', NULL),
(4, 5, '2026-01-08', '09:44:04', '09:45:41', 'Hadir', '2026-01-08 02:44:04', 'pending', NULL),
(5, 4, '2026-01-08', '09:47:27', '09:47:31', 'Hadir', '2026-01-08 02:47:27', 'pending', NULL),
(6, 7, '2026-01-08', '08:00:00', '17:00:00', 'Hadir', '2026-01-08 03:22:37', 'approved', NULL),
(7, 10, '2026-01-08', '11:24:51', '11:25:02', 'Hadir', '2026-01-08 04:24:51', 'pending', NULL),
(8, 12, '2026-01-08', '12:11:22', '12:11:27', 'Hadir', '2026-01-08 05:11:22', 'approved', NULL),
(9, 14, '2026-01-08', '12:13:07', '12:13:09', 'Hadir', '2026-01-08 05:13:07', 'approved', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `lembur`
--

CREATE TABLE `lembur` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `tanggal` date NOT NULL,
  `jam_mulai` time NOT NULL,
  `jam_selesai` time NOT NULL,
  `durasi` int DEFAULT NULL COMMENT 'Durasi dalam menit',
  `alasan_lembur` varchar(255) NOT NULL,
  `status_validasi` enum('pending','approved','rejected') DEFAULT 'pending',
  `catatan_foreman` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lembur`
--

INSERT INTO `lembur` (`id`, `user_id`, `tanggal`, `jam_mulai`, `jam_selesai`, `durasi`, `alasan_lembur`, `status_validasi`, `catatan_foreman`, `created_at`) VALUES
(1, 8, '2026-01-08', '17:00:00', '19:00:00', NULL, 'Kejar deadline project', 'pending', NULL, '2026-01-08 03:22:37');

-- --------------------------------------------------------

--
-- Table structure for table `slip_gaji`
--

CREATE TABLE `slip_gaji` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `bulan` varchar(20) NOT NULL,
  `total_gaji` decimal(12,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `slip_gaji`
--

INSERT INTO `slip_gaji` (`id`, `user_id`, `bulan`, `total_gaji`, `created_at`) VALUES
(2, 4, '2026-01', 5000000.00, '2026-01-06 06:36:54'),
(3, 5, '2026-01', 200000.00, '2026-01-08 02:46:33');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `nik` varchar(50) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','karyawan','foreman') NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `foreman_id` int DEFAULT NULL,
  `jam_masuk_standar` time DEFAULT '08:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `nik`, `username`, `email`, `password`, `role`, `created_at`, `foreman_id`, `jam_masuk_standar`) VALUES
(1, '1231231', 'Admin', 'admin@absensi.com', '$2y$10$kU6tlxcZ2uJziEptRJXs7OJzjf2vAiPdQ.yEnYUJH1x4mDjo1Bc56', 'admin', '2026-01-06 03:00:00', NULL, '08:00:00'),
(4, '1231232', 'Karyawan', 'Karyawan@gmail.com', '$2y$10$b6YkzeQyNXZMtm9c1hdZ8u2Ps1ilhoyif0WEleB2LQrh9xmIiHNDy', 'karyawan', '2026-01-06 06:17:39', NULL, '08:00:00'),
(5, '1231233', 'Yanto', 'ts@gmail.com', '$2y$10$5YsmIMYlVx8Z3prw5c3S3uwjvZHIdMdhO2ZmdT6zc0hbq4hPlCW/2', 'karyawan', '2026-01-08 02:43:09', NULL, '08:00:00'),
(6, '1231234', 'budi_foreman', 'budi@foreman.com', '$2y$10$kBJtTGhAygAIu.X3urTpnu58h515uWb/7oI9KjzUy.YPRXANi3KUm', 'foreman', '2026-01-08 03:22:37', NULL, '08:00:00'),
(7, '1231235', 'andi_team', 'andi_team@test.com', '$2y$10$9t4vdVG2zlyN.9M5DH4LFOXV4zcrM4w7maJBrI5UOvHK81riypKGC', 'karyawan', '2026-01-08 03:22:37', 6, '08:00:00'),
(8, '12312311', 'siti_team', 'siti_team@test.com', '$2y$10$9t4vdVG2zlyN.9M5DH4LFOXV4zcrM4w7maJBrI5UOvHK81riypKGC', 'karyawan', '2026-01-08 03:22:37', 6, '08:00:00'),
(9, '12312310', 'tresna', 'tresna@gmail.com', '$2y$10$38kl9h64LFy9Skks7ql9De1FyxKg1gYvCcgpy.ffKdIMRLXhpRms.', 'karyawan', '2026-01-08 04:23:17', NULL, '08:00:00'),
(10, '1231239', 'Fuad', 'fuad@gmail.com', '$2y$10$U4e.96huth9S5FwhaqE7.O98.1V6u9Iel.yadh9K3VtA1H1MGo4CK', 'karyawan', '2026-01-08 04:23:59', NULL, '08:00:00'),
(11, '1231238', 'fikri', 'fikri@gmail.com', '$2y$10$PEh2KOX1x7nZNxTUGA4VeOJzmEU6a7jLciBTUR4lCBcCZqSugByGO', 'karyawan', '2026-01-08 04:35:28', 6, '08:00:00'),
(12, '1231237', 'jakaria', 'jakaria@gmail.com', '$2y$10$btUSFFMq85MV7rI.FeWTbuZ0n4TTwlAMivr13V93.6LjwUGofnhyO', 'karyawan', '2026-01-08 04:36:47', 6, '08:00:00'),
(14, '12399321', 'nursidik', 'nursidik@gmail.com', '$2y$10$eUhThqL7QQNnqaI22C4WCO.QShzFj5a6OwbWdaFdQtImxhrF6Mu26', 'karyawan', '2026-01-08 05:12:43', 6, '08:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absensi`
--
ALTER TABLE `absensi`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_absensi_harian` (`user_id`,`tanggal`);

--
-- Indexes for table `lembur`
--
ALTER TABLE `lembur`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `slip_gaji`
--
ALTER TABLE `slip_gaji`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_gaji_bulanan` (`user_id`,`bulan`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `nik` (`nik`),
  ADD KEY `fk_users_foreman` (`foreman_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `absensi`
--
ALTER TABLE `absensi`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `lembur`
--
ALTER TABLE `lembur`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `slip_gaji`
--
ALTER TABLE `slip_gaji`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `absensi`
--
ALTER TABLE `absensi`
  ADD CONSTRAINT `fk_absensi_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `lembur`
--
ALTER TABLE `lembur`
  ADD CONSTRAINT `lembur_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `slip_gaji`
--
ALTER TABLE `slip_gaji`
  ADD CONSTRAINT `fk_gaji_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_foreman` FOREIGN KEY (`foreman_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
