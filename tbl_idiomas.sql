
CREATE TABLE `tbl_idiomas` (
  `idIdioma` int(11) NOT NULL AUTO_INCREMENT,
  `prefijo` varchar(5) NOT NULL,
  `idioma` varchar(50) NOT NULL,
  PRIMARY KEY (`idIdioma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `tbl_idiomas` WRITE;
/*!40000 ALTER TABLE `tbl_idiomas` DISABLE KEYS */;

INSERT INTO `tbl_idiomas` (`idIdioma`, `prefijo`, `idioma`)
VALUES
	(1,'es','Español'),
	(2,'en','Inglés'),
	(3,'fr','Francés'),
	(4,'de','Alemán'),
	(5,'ko','Coreano'),
	(6,'pt','Portugués');