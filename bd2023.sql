/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.32-MariaDB : Database - tesis2023
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`tesis2023` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `tesis2023`;

/*Table structure for table `lectura` */

DROP TABLE IF EXISTS `lectura`;

CREATE TABLE `lectura` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `ubicacion_id` varchar(255) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL,
  `sensor_1` varchar(255) DEFAULT NULL,
  `sensor_2` double DEFAULT NULL,
  `sensor_3` varchar(255) DEFAULT NULL,
  `sensor_4` double DEFAULT NULL,
  `sensor_5` varchar(255) DEFAULT NULL,
  `sensor_6` double DEFAULT NULL,
  `sensor_7` varchar(255) DEFAULT NULL,
  `sensor_8` double DEFAULT NULL,
  `sensor_9` double DEFAULT NULL,
  `latitud` varchar(50) DEFAULT NULL,
  `longitud` varchar(50) DEFAULT NULL,
  `leido` varchar(50) DEFAULT NULL COMMENT 'SI leido - NO leido',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `lectura` */

insert  into `lectura`(`id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_2`,`sensor_3`,`sensor_4`,`sensor_5`,`sensor_6`,`sensor_7`,`sensor_8`,`sensor_9`,`latitud`,`longitud`,`leido`) values (1,'1','2019-12-17 09:37:15','False',0,'31°32\'22.7\"S 68°32\'10.4\"W',0,'True',0.8,'metano 0ppm, butano 0ppm, humo 0ppm',34,80,'-31.53963888888889','-68.53622222222222','NO'),(2,'2','2019-12-17 09:37:18','True',0,'31°32\'23.9\"S 68°30\'47.8\"W',0.1,'True',0.7,'metano 0ppm, butano 0ppm, humo 0ppm',34,12,'-31.539972222222225','-68.51327777777777','NO'),(3,'3','2019-12-17 09:37:21','False',0,'31°32\'22.8\"S 68°34\'39.9\"W',0,'True',0.9,'metano 0ppm, butano 0ppm, humo 0ppm',34.2,21,'-31.53966666666667','-68.57775','NO'),(4,'1','2019-12-17 09:37:23','False',0.67,'31°32\'15.0\"S 68°32\'54.0\"W',0,'True',0.9,'metano 0ppm, butano 0ppm, humo 0ppm',34,675,'-31.5375','-68.54833333333333','NO'),(5,'2','2019-12-17 09:37:34','False',0,'31°31\'47.9\"S 68°35\'48.2\"W',0,'True',0.8,'metano 0ppm, butano 0ppm, humo 0ppm',34.1,265,'-31.52997222222222','-68.59672222222221','NO'),(6,'3','2019-12-17 09:37:37','True',0.54,'31°32\'22.7\"S 68°32\'10.4\"W',0.7,'True',0.8,'metano 0ppm, butano 250ppm, humo 0ppm',20,250.4,'-31.53963888888889','-68.53622222222222','NO'),(7,'1','2019-12-17 09:37:39','False',0.2,'31°32\'23.9\"S 68°30\'47.8\"W',0.24,'True',0.1,'metano 239ppm, butano 150ppm, humo 12ppm',34,129,'-31.539972222222225','-68.51327777777777','NO'),(8,'2','2019-12-17 09:37:41','True',0,'31°32\'22.8\"S 68°34\'39.9\"W',0,'True',0.1,'metano 0ppm, butano 0ppm, humo 0ppm',21,80,'-31.53966666666667','-68.57775','NO'),(9,'3','2019-12-17 09:38:11','True',0.67,'31°32\'15.0\"S 68°32\'54.0\"W',0,'False',0.2,'metano 0ppm, butano 0ppm, humo 390ppm',20,345,'-31.5375','-68.54833333333333','NO'),(10,'1','2019-12-17 09:38:13','False',0,'31°31\'47.9\"S 68°35\'48.2\"W',0.5,'False',0,'metano 0ppm, butano 0ppm, humo 0ppm',15,30.45,'-31.52997222222222','-68.59672222222221','NO');

/*Table structure for table `lectura1` */

DROP TABLE IF EXISTS `lectura1`;

CREATE TABLE `lectura1` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `ubicacion_id` varchar(255) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL,
  `sensor_1` varchar(255) DEFAULT NULL,
  `sensor_2` double DEFAULT NULL,
  `sensor_3` varchar(255) DEFAULT NULL,
  `sensor_4` double DEFAULT NULL,
  `sensor_5` varchar(255) DEFAULT NULL,
  `sensor_6` double DEFAULT NULL,
  `sensor_7` varchar(255) DEFAULT NULL,
  `sensor_8` double DEFAULT NULL,
  `sensor_9` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `lectura1` */

insert  into `lectura1`(`id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_2`,`sensor_3`,`sensor_4`,`sensor_5`,`sensor_6`,`sensor_7`,`sensor_8`,`sensor_9`) values (1,'id1','0000-00-00 00:00:00','false',0,'-31.5395004,-68.5368743',0,'true',0.8,'metano 0ppm, butano 0ppm, humo 0ppm',34,80),(2,'id2','0000-00-00 00:00:00','false',0,'-31.5394094,-68.5130417',0.1,'true',0.7,'metano 0ppm, butano 0ppm, humo 0ppm',34,12),(3,'id3','0000-00-00 00:00:00','false',0,'-31.5411137,-68.5776381',0,'true',0.9,'metano 0ppm, butano 0ppm, humo 0ppm',34.2,21),(4,'id4','0000-00-00 00:00:00','false',0.67,'-31.5371463,-68.5479689',0,'treu',0.9,'metano 0ppm, butano 0ppm, humo 0ppm',34,675),(5,'id5','0000-00-00 00:00:00','false',0,'-31.5395004,-68.5368743',0,'true',0.8,'metano 0ppm, butano 0ppm, humo 0ppm',34.1,265),(6,'id1','0000-00-00 00:00:00','true',0.54,'-31.5395004,-68.5368743',0.7,'true',0.8,'metano 0ppm, butano 250ppm, humo 0ppm',20,250.4),(7,'id2','0000-00-00 00:00:00','false',0.2,'-31.5394094,-68.5130417',0.24,'true',0.1,'metano 239ppm, butano 150ppm, humo 12ppm',34,129),(8,'id3','0000-00-00 00:00:00','true',0,'-31.5411137,-68.5776381',0,'true',0.1,'metano 0ppm, butano 0ppm, humo 0ppm',21,80),(9,'id4','0000-00-00 00:00:00','true',0.67,'-31.5371463,-68.5479689',0,'false',0.2,'metano 0ppm, butano 0ppm, humo 390ppm',20,345),(10,'id5','0000-00-00 00:00:00','false',0,'-31.5298923,-68.5967097',0.5,'false',0,'metano 0ppm, butano 0ppm, humo 0ppm',15,30.45);

/*Table structure for table `permiso` */

DROP TABLE IF EXISTS `permiso`;

CREATE TABLE `permiso` (
  `idpermiso` int(4) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`idpermiso`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `permiso` */

insert  into `permiso`(`idpermiso`,`nombre`) values (1,'Usuario'),(2,'Dataset'),(3,'Preguntas'),(4,'Respuestas'),(5,'Criterios'),(6,'Subcriterios'),(7,'Permisos'),(8,'Evaluacion'),(9,'Resultado');

/*Table structure for table `sensor` */

DROP TABLE IF EXISTS `sensor`;

CREATE TABLE `sensor` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `tipovalor` varchar(255) DEFAULT NULL,
  `prioridad` double DEFAULT NULL,
  `valormin` varchar(255) DEFAULT NULL,
  `valormax` varchar(255) DEFAULT NULL,
  `alerta` varchar(255) DEFAULT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `sensor` */

insert  into `sensor`(`id`,`codigo`,`descripcion`,`tipovalor`,`prioridad`,`valormin`,`valormax`,`alerta`,`comentarios`) values (1,'sensor_1','Sensor de llama Ky-026','Booleano',1,'FALSE','TRUE','red','Sensor 1 – de llama o fuego – booleano - True o False  - Prioridad 1'),(2,'sensor_2','Sensor Polvo Gp2y1014','Double',0,NULL,NULL,NULL,NULL),(3,'sensor_3','Módulo GPS NEO-6M','String',0,NULL,NULL,NULL,NULL),(4,'sensor_4','Sensor De Humedad Y Temperatura Dht22 ','Double o con librería String',4,NULL,NULL,NULL,'Sensor 4 – de Humedad – numérico -  ¿me falta los valores de referencia?  - Prioridad 4'),(5,'sensor_5','Sensor Detector Movimiento Infrarrojo Sr501','Booleano',3,'FALSE','TRUE','red','Sensor 5 – de movimiento – booleano -  True o False  - Prioridad 3'),(6,'sensor_6','Sensor De Luz Ambiental Breakout Temt6000 ','double',0,NULL,NULL,NULL,NULL),(7,'sensor_7','Sensor Metano Butano Humo Mq2','double',0,NULL,NULL,NULL,NULL),(8,'sensor_8','Sensor De Temperatura Infrarrojo Mlx90614 ','Double',2,'49','50','red','Sensor 8 – de temperatura –  numérico - valores mayores a 50º   - Prioridad 2'),(9,'sensor_9','Sensor Ultrasonido HC-SR04','Mide distancia. Double',0,NULL,NULL,NULL,NULL);

/*Table structure for table `sensor1` */

DROP TABLE IF EXISTS `sensor1`;

CREATE TABLE `sensor1` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(90) DEFAULT NULL,
  `descripcion` varchar(90) DEFAULT NULL,
  `tipodatos` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `sensor1` */

insert  into `sensor1`(`id`,`codigo`,`descripcion`,`tipodatos`) values (1,'sensor1','Sensor de llama Ky-026','Booleano'),(2,'sensor2','Sensor Polvo Gp2y1014','Double');

/*Table structure for table `ubicacion` */

DROP TABLE IF EXISTS `ubicacion`;

CREATE TABLE `ubicacion` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(90) DEFAULT NULL,
  `domicilio` varchar(90) DEFAULT NULL,
  `departamento` varchar(90) DEFAULT NULL,
  `latitud` varchar(90) DEFAULT NULL,
  `longitud` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `ubicacion` */

insert  into `ubicacion`(`id`,`nombre`,`domicilio`,`departamento`,`latitud`,`longitud`) values (1,'Centro Civico','Libertador y España','Capital','-31.536160','-68.537441'),(2,'Centro Cultural Conte Grand','San Luis, Las Heras Norte y, J5400 San Juan','Capital','-31.5351038','-68.5403271'),(3,'Museo Provincial de Bellas Artes Franklin Rawson','Av. Libertador Gral. San Martín 902, San Juan','Capital','-31.5355123','-68.5400917');

/*Table structure for table `usuario` */

DROP TABLE IF EXISTS `usuario`;

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo_documento` varchar(20) NOT NULL,
  `num_documento` varchar(20) NOT NULL,
  `direccion` varchar(70) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `cargo` varchar(20) DEFAULT NULL,
  `usuario` varchar(20) NOT NULL,
  `clave` varchar(64) NOT NULL,
  `imagen` varchar(50) NOT NULL,
  `condicion` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_UNIQUE` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `usuario` */

insert  into `usuario`(`id`,`nombre`,`tipo_documento`,`num_documento`,`direccion`,`telefono`,`email`,`cargo`,`usuario`,`clave`,`imagen`,`condicion`) values (1,'rmolina','DNI','xxxxxxxxxxxx','xxxxxxxxxxx','931742904','robertomolina999@hotmail.com','','admin','202cb962ac59075b964b07152d234b70','1526654254.png',1);

/*Table structure for table `usuario_permiso` */

DROP TABLE IF EXISTS `usuario_permiso`;

CREATE TABLE `usuario_permiso` (
  `idusuario_permiso` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) DEFAULT NULL,
  `idpermiso` int(11) DEFAULT NULL,
  PRIMARY KEY (`idusuario_permiso`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `usuario_permiso` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
