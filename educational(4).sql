/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : educational

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 08/01/2021 11:57:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `admin` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '账号',
  `password` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `salt` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '加密盐',
  `level` tinyint(1) NOT NULL COMMENT '1，超级管理员，2老师',
  `name` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '是否启用',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 44 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'admin', '516eb11bbeb8a504dda4fd1198e042d7', 'e625fb438d13f7f6defbbacb1f0a6d84', 1, '管理员', 1);
INSERT INTO `admin` VALUES (31, '3bQPve', 'e93fe7552778ded9c169ec54bcafa632', '1aaac9251c500fb3a4bcdce9d21ff8ce', 2, '最小22', 1);
INSERT INTO `admin` VALUES (32, '8rjZF3', '779fbba718592493009dbfb9f5032e90', 'a7a3b3cfac70baf20f3ab56f03bd2142', 2, '一二三', 0);
INSERT INTO `admin` VALUES (34, 'z7KJXm', 'add79aa0fd47d468ed47699171a4bd34', '9351cab7ba7db8459102f049e199fe31', 2, '大老师', 1);
INSERT INTO `admin` VALUES (35, 'cQSPdf', '77e8b39a096fb3984f1985e6baf29674', 'f522a8eb6b9471f49786376d599248f1', 2, '大哥', 1);
INSERT INTO `admin` VALUES (36, 'cQSPdf1', 'a59245e544687566963af957c772e987', '3b279677c720dd3e9741a11592c8144a', 2, '大哥223', 1);
INSERT INTO `admin` VALUES (37, 'LUAsZ4', '0a7ec5b8b2f868349983b85386118072', '3ecb8e363b8d2ac3171b2aadf457a93c', 2, 'NV', 1);
INSERT INTO `admin` VALUES (38, '5ExnyV', 'ec8bc708c09ce7950464e574f160e84f', '8a25ad0ceda51ae7f9497256b19bade3', 2, 'z5', 1);
INSERT INTO `admin` VALUES (39, 'DtH8Xa', '15755d9a48ee6ae8d4b44fabcbeb517b', '7870a422703d8025b105730dfff2ccd9', 2, 'gN', 1);
INSERT INTO `admin` VALUES (40, 'Uv9JeQ', '21b028be8fefc04919e0cb83a337a79e', '01e7616debdebfd4e9f3c78c5716027f', 2, 'BA', 1);
INSERT INTO `admin` VALUES (41, 'gH8DcY', 'ed095fbfeeaf6f649bf4c007bff80e58', '8d3060365adde62c3aa636fded3d7f60', 2, 'wJ', 1);
INSERT INTO `admin` VALUES (42, 'jyHXTa', '2dd97cd23aee6558adb13b160f2bc456', '8cd0123d78b000789312a4fec575e0ee', 2, '最大', 1);
INSERT INTO `admin` VALUES (43, 'J6eXsZ', 'b6e851e84e9df8b612396bfe8df15f9e', '01976fbe4dba7ba7cfb22fa0e579f642', 2, '最新', 1);

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '班级名字',
  `t_id` int(0) NOT NULL COMMENT '班级管理老师',
  `addtime` int(0) NOT NULL COMMENT '添加时间',
  `user_count` int(0) NOT NULL COMMENT '班级学生人数',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id`(`id`) USING BTREE,
  INDEX `t_id`(`t_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班级' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (2, '二班', 42, 1600760130, 2);
INSERT INTO `class` VALUES (4, '三班', 36, 1607061051, 4);

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `id` int(0) NOT NULL,
  `c_id` int(0) NOT NULL COMMENT '课程id',
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '课程名',
  `college` char(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '院系',
  `credit` int(0) NOT NULL COMMENT '学分',
  `semester_hour` int(0) NOT NULL COMMENT '学时',
  `number` int(0) NOT NULL COMMENT '人数',
  `time` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '上课时间',
  `local` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '上课地点',
  `info` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '简介',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `c_id`(`c_id`) USING BTREE,
  INDEX `id`(`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, 1, '语文', '文法学院', 4, 64, 20, '第1周到第14周，星期一，第1节到第4节', '教103', '语文');
INSERT INTO `course` VALUES (2, 2, '英语', '文法学院', 4, 64, 20, '第1周到第14周，星期二，第6节到第9节', '教203', 'English');
INSERT INTO `course` VALUES (3, 3, '数学', '理学院', 5, 80, 20, '第1周到第16周，星期三，第1节到第4节', '教302', '数学');
INSERT INTO `course` VALUES (4, 4, '程序设计', '信息学院', 4, 64, 30, '第1周到第14周，星期四，第6节到第9节', '科103', '程序');
INSERT INTO `course` VALUES (5, 5, '历史', '历史学院', 2, 32, 10, '第5周到第12周，第10节到第12节', '科503', '历史');

-- ----------------------------
-- Table structure for evaluation
-- ----------------------------
DROP TABLE IF EXISTS `evaluation`;
CREATE TABLE `evaluation`  (
  `id` int(0) NOT NULL,
  `uid` int(0) NOT NULL COMMENT '学生id',
  `tid` int(0) NOT NULL COMMENT '老师id',
  `c_id` int(0) NOT NULL COMMENT '课程id',
  `score1` int(0) NOT NULL COMMENT '教学态度',
  `score2` int(0) NOT NULL COMMENT '教学效果',
  `score3` int(0) NOT NULL COMMENT '作业安排',
  `score4` int(0) NOT NULL COMMENT '教案准备',
  `score5` int(0) NOT NULL COMMENT '道德规范',
  `commit` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '评论',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uid`(`uid`) USING BTREE,
  INDEX `tid`(`tid`) USING BTREE,
  INDEX `c_id1`(`c_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of evaluation
-- ----------------------------
INSERT INTO `evaluation` VALUES (1, 1, 35, 4, 5, 5, 5, 5, 5, '认真负责，讲的好');
INSERT INTO `evaluation` VALUES (2, 2, 34, 5, 5, 5, 5, 5, 5, NULL);

-- ----------------------------
-- Table structure for paperselection
-- ----------------------------
DROP TABLE IF EXISTS `paperselection`;
CREATE TABLE `paperselection`  (
  `id` int(0) NOT NULL,
  `uid` int(0) NOT NULL COMMENT '学生id',
  `tid` int(0) NOT NULL COMMENT '老师id',
  `topic` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '选题题目',
  `info` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '简介',
  `status` int(0) NOT NULL COMMENT '选题状态，0为未选，1为已选',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uid1`(`uid`) USING BTREE,
  INDEX `tid2`(`tid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of paperselection
-- ----------------------------
INSERT INTO `paperselection` VALUES (1, 1, 35, 'web开发', 'web，js，php', 1);
INSERT INTO `paperselection` VALUES (2, 2, 34, '唐朝历史研究', '唐朝', 0);

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `uid` int(0) NOT NULL COMMENT '学生id',
  `k_time` int(0) NOT NULL COMMENT '考试时间',
  `score` float(3, 1) NOT NULL COMMENT '分数',
  `kskc` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '考试课程',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uid3`(`uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '分数表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES (1, 1, 1607011200, 80.0, '语文');
INSERT INTO `score` VALUES (2, 2, 1607011200, 20.5, '语文');
INSERT INTO `score` VALUES (3, 3, 1607011200, 81.0, '语文');
INSERT INTO `score` VALUES (4, 7, 1607011200, 81.5, '语文');
INSERT INTO `score` VALUES (5, 1, 1606924800, 80.0, '数学');
INSERT INTO `score` VALUES (6, 2, 1606924800, 80.5, '数学');
INSERT INTO `score` VALUES (7, 3, 1606924800, 88.5, '数学');
INSERT INTO `score` VALUES (9, 5, 1606838400, 50.0, '英语');
INSERT INTO `score` VALUES (10, 6, 1606838400, 95.5, '英语');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `code` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学号',
  `cid` char(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '身份证',
  `in_time` int(0) NOT NULL COMMENT '入学时间',
  `out_time` int(0) NOT NULL COMMENT '离开学校时间',
  `info` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '简介',
  `l_name` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '联系人',
  `l_phone` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '联系人手机',
  `l2_name` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '备用联系人',
  `l2_phone` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '备用联系人手机',
  `add` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '住址',
  `class_id` int(0) NOT NULL COMMENT '班级id',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cid`(`cid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学生' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '张五', '2020124152300', '513723199112023637', 1607011200, 0, '是个好学生哦', '贞观三年', '18888888888', '张三姆', '15555555555', '什么路什么号', 4);
INSERT INTO `student` VALUES (2, '李斯打赏', '2020124152444', '513723199112023636', 1606838400, 0, '', '李斯爸爸', '18888888888', '', '0', '0', 4);
INSERT INTO `student` VALUES (3, '王五1', '2020124152717', '513723199112023639', 1607356800, 1609430400, '', '搜索', '18888888888', '啊啊', '', '', 4);
INSERT INTO `student` VALUES (5, '123', '2020124164340', '513723199112023635', 1606752000, 0, '', '123', '18888888888', '', '', '', 2);
INSERT INTO `student` VALUES (6, '123', '2020124164340', '513723199112023638', 1606752000, 0, '', '123', '18888888888', '', '', '', 2);
INSERT INTO `student` VALUES (7, '123', '2020124164340', '513723199112023739', 1606752000, 0, '', '123', '18888888888', '', '', '', 4);

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `a_id` int(0) NOT NULL COMMENT '账号id',
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `cid` char(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '身份证',
  `in_time` int(0) NOT NULL COMMENT '入职时间',
  `out_time` int(0) NOT NULL COMMENT '离职时间',
  `oa_time` int(0) NOT NULL COMMENT '合同到期时间',
  `info` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '简介',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `a_id`(`a_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '教师' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES (12, 31, '数学老师', '513723199112024631', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (13, 32, '英语老师', '513723199112024632', 0, 1608739200, 1608912000, '');
INSERT INTO `teacher` VALUES (15, 34, '历史老师', '513723199112024633', 1606838400, 1608825600, 1609344000, '<p>萨达</p>');
INSERT INTO `teacher` VALUES (16, 35, 'c语言老师', '513723199112024634', 1609344000, 1607011200, 1606924800, '<p>啦啦啦</p>');
INSERT INTO `teacher` VALUES (17, 36, '语文老师', '513723199112024635', 1606924800, 1607011200, 1606924800, '<p>啦啦啦2</p>');
INSERT INTO `teacher` VALUES (18, 37, 'NV', '513723199112024635', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (19, 38, 'z5', '513723199112024635', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (20, 39, 'gN', '513723199112024635', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (21, 40, 'BA', '513723199112024635', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (22, 41, 'wJ', '513723199112024635', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (23, 42, '最大', '513723199112024635', 0, 0, 0, '');
INSERT INTO `teacher` VALUES (24, 43, '最新', '513723199112024635', 0, 0, 0, '');

SET FOREIGN_KEY_CHECKS = 1;
