/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 100428 (10.4.28-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : appoinment

 Target Server Type    : MySQL
 Target Server Version : 100428 (10.4.28-MariaDB)
 File Encoding         : 65001

 Date: 20/03/2024 04:28:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for appoinments
-- ----------------------------
DROP TABLE IF EXISTS `appoinments`;
CREATE TABLE `appoinments`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `surname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `telephone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `representation` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of appoinments
-- ----------------------------
INSERT INTO `appoinments` VALUES (1, 'Nimesh Priyankara', 'Muthuwadige', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (2, 'Danushika Nayomi', 'Thalagala Achchige', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (3, 'Madusanka Lakmal Abewardhana', 'Abewardhana Mudiyanselage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (4, 'Chandrawansha Jayasinghe', 'Yaddehi Gedara', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (5, 'Pradeep Chaminda', 'Hewavitharanage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (6, 'Samith Ranga Shiroshan', 'Hewa Ranasinghege', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (7, 'Mahinsas Gayan Jayathunga', 'Rankothge', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (8, 'Hangriwort Asela', 'Peramunage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (9, 'Kelum Sampath Rathnayaka', 'Upasinghe Arachchilage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (10, 'Posintha Hasindu Marasinha', 'Athugalge', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (11, 'Upul Kumara', 'Wakkumbure Gedara Gunarathna', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (12, 'Indika Anura Kumara Jayalath', 'Walimuni Dewayalage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (13, 'Shehan Prasanna ', 'Gothatuge', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (14, 'Asela Rathnayaka', 'Rathnayaka Mudiyanselage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (15, 'Sisil Prasanna Hewapola', 'Wimalge', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (16, 'Indika Lanka Dayarathna', 'Solanga Arachchige', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (17, 'Indika Ruwan Kumara Kularathne', 'Sri Buwanekabahu Makaradwaja Dewanarayana Chitra Mohottalalage Walawwe', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (18, 'Dewapriya Aberathna', 'Deldeniye Maha Mudiyanselage Walawwe', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (19, 'Dissanayaka Mudiyanselage Kumara Thilaka', 'Samarakoon', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (20, 'Thushika Thilakshi Perera', 'Imiya Kankanamalage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (21, 'Nishantha ', 'Liyanage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (22, 'Vijitha Dhammika', 'Colomba Munasingha Arachchige', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (23, 'Kawan Ranga', 'Kuruppu', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (24, 'Priyankara Madushan Gunasinghe', 'Uruliyanage Don', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (25, 'Janaka Aruna Kumara', 'Thelkara Gedara Sumed', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (26, 'Chaminda Kumara Hangawatta', 'Naranapiti Hangawatta Appuhamilage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (27, 'Gayan Buddhika Jayakody', 'Jayakody Kankanamalage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (28, 'Dilshan Madhushanka', 'Alagiya Durage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (29, 'Dinesh Kumar', 'Premkumar', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (30, 'Sachith Madushanka', 'Abeynayakage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (31, 'Shamith Ruwan', 'Mayadunnage Don', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (32, 'Chandana Dinesh', 'Kumanayaka', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (33, 'Akila Ravindra Wijesinhe', 'Demansalage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (34, 'Kapila Gunasekara', 'Menik Mudiyanselage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (35, 'Manjula Kumara', 'Kandana Arachchige', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (36, 'Dinesh Kumar', 'Thachchana Moorthy', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (37, 'Asoka Weerasinghe', 'Ihala Gedara', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (38, 'Shirly Herman Susantha', 'Walpita Gamage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (39, 'Dhanushka Dilshan', 'Hewawitharana', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (40, 'Rakitha Agbo Nandarathna', 'Madamawickrama', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (41, 'Kapila Hemantha Paththuwe Arachchi', 'Paththuwe Arachchilage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (42, 'Chaminda Dilip Kumara Rupasinghe', 'Basnayaka Aracchilage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (43, 'Sheron Dilrukshi Thennekoon', 'Thennekoon', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (44, 'Shyanaka Suranga Perera', 'Nedagamuwage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (45, 'Chaminda', 'Gampalage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (46, 'Kushan Srilal Kumara', 'Hewa Kalukapuge', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (47, 'Krisma Melani Gamalath', 'Gamalath Kankanamalage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (48, 'Madusanka Praneeth Padmalal Mamuhewa', 'Mamu Hewage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (49, 'Sanjaya Kumara Chathuranga', 'Amuwala Dewage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (50, 'Lumidu Pradeepana', 'Hettiarachchige Don', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (51, 'Maselas Shimantha Fernando', 'Mihindukulasuriya', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (52, 'Thusara Manoj Kumara', 'Mudiyanselage Gedara', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (53, 'Sanjaya Dilantha Kumara Samarajeewa', 'Siyambalagaha Gedara', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (54, 'Darshana Bandara Premarathna', 'Wanni Adipaththu Mudiyanselage', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (55, 'Harshila Kavindi', 'Kodithuwakku Arachchige', NULL, NULL, 'Assistant');
INSERT INTO `appoinments` VALUES (56, 'Sachintha Dilshan', 'Rajapaksha Arachchige', NULL, NULL, 'Assistant');

SET FOREIGN_KEY_CHECKS = 1;
