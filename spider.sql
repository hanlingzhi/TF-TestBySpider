/*
 Navicat Premium Data Transfer

 Source Server         : 本机-root
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : hanlingzhi

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 15/03/2020 13:58:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ali_yun_product
-- ----------------------------
DROP TABLE IF EXISTS `ali_yun_product`;
CREATE TABLE `ali_yun_product` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `category1` varchar(255) DEFAULT NULL COMMENT '一级类目',
  `category2` varchar(255) DEFAULT NULL COMMENT '二级类目',
  `title` varchar(255) DEFAULT NULL COMMENT '题目',
  `link` varchar(255) DEFAULT NULL COMMENT '类目链接',
  `description` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '类目介绍',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=275 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `tid` bigint DEFAULT NULL COMMENT '任务ID',
  `pid` bigint DEFAULT NULL COMMENT '产品ID',
  `pic_new` varchar(255) DEFAULT NULL COMMENT '新图片地址',
  `pic_old` varchar(255) DEFAULT NULL COMMENT '老图片地址',
  `pl_ssim` decimal(20,17) DEFAULT NULL COMMENT 'PL相似度',
  `cv_ssim` decimal(20,17) DEFAULT NULL COMMENT 'CV相似度',
  `pic_pl_diff` varchar(255) DEFAULT NULL COMMENT 'PL差异图',
  `pic_oc_diff` varchar(255) DEFAULT NULL COMMENT 'CV差异图',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `old_ssim` decimal(20,17) DEFAULT NULL COMMENT '前三次历史相似度',
  `result` tinyint DEFAULT '0' COMMENT 'case结果 0待定 1 通过 2失败',
  `reason` varchar(255) DEFAULT NULL COMMENT '失败原因',
  PRIMARY KEY (`id`),
  KEY `tid_foreign` (`tid`),
  KEY `pid_foreign` (`pid`),
  CONSTRAINT `pid_foreign` FOREIGN KEY (`pid`) REFERENCES `ali_yun_product` (`id`),
  CONSTRAINT `tid_foreign` FOREIGN KEY (`tid`) REFERENCES `task` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
