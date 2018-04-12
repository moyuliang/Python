/*
Navicat MySQL Data Transfer

Source Server         : python_study
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : studypy

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-04-12 22:40:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bank
-- ----------------------------
DROP TABLE IF EXISTS `bank`;
CREATE TABLE `bank` (
  `account` int(11) NOT NULL,
  `money` int(11) DEFAULT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bank
-- ----------------------------
INSERT INTO `bank` VALUES ('3', '500');
INSERT INTO `bank` VALUES ('7', '40');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '佟湘玉');
INSERT INTO `user` VALUES ('2', '白展堂');
INSERT INTO `user` VALUES ('3', '郭芙蓉');
INSERT INTO `user` VALUES ('4', '吕轻侯');
INSERT INTO `user` VALUES ('5', '李大嘴');
INSERT INTO `user` VALUES ('6', '邢育森');
INSERT INTO `user` VALUES ('7', '燕小六');
INSERT INTO `user` VALUES ('8', '白玉汤');
