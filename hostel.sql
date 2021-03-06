
/*
IF EXISTS in drop table will eliminate errors and generates a note for nonexixting tables.
Creates table academic_info - ainfo with student id as primary key.
Lock the tables with write permissions.
Insert values into the table and unlock the tables
*/


DROP TABLE IF EXISTS `ainfo`;
CREATE TABLE `ainfo` (
  `studentID` varchar(9) DEFAULT NULL,
  `year` int(1) DEFAULT NULL,
  `cgpa` float(4,2) DEFAULT NULL,
  `credits` int(11) DEFAULT NULL,
  KEY `a_sid` (`studentID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

LOCK TABLES `ainfo` WRITE;
INSERT INTO `ainfo` VALUES ('15BCE0001',1,8.40,47),('15BCE0002',1,7.60,45),('15BCE0003',1,9.20,44),('15BCE0004',1,7.60,42),('15BCE0005',1,8.80,45),('15BCE0006',1,8.00,47),('14BME0001',2,7.60,93),('14BME0002',2,8.80,95),('14BME0003',2,9.40,90),('14BME0004',2,7.40,96),('13BME0004',3,7.20,140),('13BME0003',3,7.00,144),('13BME0002',3,8.40,140),('13BME0001',3,7.40,136),('12BME0001',4,7.40,167),('12BME0002',4,7.40,173),('12BME0003',4,6.40,170),('12BME0004',4,8.00,168);
UNLOCK TABLES;

/*
IF EXISTS in drop table will eliminate errors and generates a note for nonexixting tables.
Creates table Personal_info - pinfo with student id as primary key.
Lock the tables with write permissions.
*/

DROP TABLE IF EXISTS `pinfo`; 
CREATE TABLE `pinfo` (
  `studentID` varchar(9) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `phNo` int(10) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `stay` char(1) DEFAULT NULL,
  KEY `a_sid` (`studentID`)wq
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

LOCK TABLES `pinfo` WRITE;
UNLOCK TABLES;

/*
IF EXISTS in drop table will eliminate errors and generates a note for nonexixting tables.
Creates table room with room id as primary key.
Lock the tables with write permissions.
Insert values into the table and unlock the tables
*/

DROP TABLE IF EXISTS `room`;

CREATE TABLE `room` (
  `roomid` int(4) NOT NULL,
  `Type` char(1) DEFAULT NULL,
  `beds` int(1) DEFAULT NULL,
  `block` char(1) DEFAULT NULL,
  `rno` int(3) DEFAULT NULL,
  `taken` int(1) DEFAULT NULL,
  PRIMARY KEY (`roomid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

LOCK TABLES `room` WRITE;
INSERT INTO `room` VALUES (1001,'A',6,'K',1,0),(1002,'A',4,'K',2,0),(1004,'N',1,'K',4,0),(1003,'N',6,'K',3,0),(2001,'A',2,'L',1,0),(2002,'A',4,'L',2,0),(2003,'N',2,'L',3,0),(2004,'A',1,'L',4,0),(3001,'N',6,'M',1,0),(3002,'A',4,'M',2,0),(3003,'A',1,'M',3,0),(4001,'N',2,'N',1,0),(4002,'A',4,'N',2,0),(1005,'A',6,'K',5,0),(1006,'A',4,'K',6,0),(1007,'N',6,'K',7,0),(1008,'N',4,'K',8,0),(1009,'A',2,'K',9,0),(1010,'N',2,'K',10,0),(1011,'A',2,'K',11,0),(2005,'A',6,'L',5,0),(2006,'A',6,'L',6,0),(2007,'N',6,'L',7,0),(2008,'N',4,'L',8,0),(2009,'A',4,'L',9,0),(2010,'A',4,'L',10,0),(2011,'A',2,'L',11,0),(2012,'N',2,'L',12,0);
UNLOCK TABLES;

/*
IF EXISTS in drop table will eliminate errors and generates a note for nonexixting tables.
Creates student table with student id as primary key.
Lock the tables with write permissions. 
Insert values into the table and unlock the tables
*/

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `studentID` varchar(9) NOT NULL,
  `password` varchar(15) DEFAULT NULL,
  `roomID` int(4) DEFAULT NULL,
  PRIMARY KEY (`studentID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

LOCK TABLES `student` WRITE;
INSERT INTO `student` VALUES ('15BCE0001','QWERTY',NULL),('15BCE0002','ASDFG',NULL),('15BCE0003','ZXCVB',NULL),('15BCE0004','WERTYU',NULL),('15BCE0005','SDFGHJ',NULL),('15BCE0006','XCVBN',NULL),('14BME0001','QWASZX',NULL),('14BME0002','WESDXC',NULL),('14BME0003','ERDFCV',NULL),('14BME0004','RTFGVB',NULL),('13BME0001','TREWQ',NULL),('13BME0002','ERTYU',NULL),('13BME0003','SDFGH',NULL),('12BME0001','ZXCASD',NULL),('12BME0002','QWEASD',NULL),('12BME0003','QQWASD',NULL),('12BME0004','QQERWASD',NULL),('13BME0004','DFGHH',NULL);
UNLOCK TABLES;
