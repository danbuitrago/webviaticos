-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `idusuarios` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(45) NOT NULL,
  `contrasena` VARCHAR(45) NOT NULL,
  `rol` VARCHAR(45) NOT NULL,
  `regional` VARCHAR(45) NOT NULL,
  `cargo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusuarios`),
  UNIQUE INDEX `idusuarios_UNIQUE` (`idusuarios` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`solicitudes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`solicitudes` (
  `idsolicitudes` INT NOT NULL,
  `fechasolicitud` DATETIME NOT NULL,
  `solicitante` VARCHAR(45) NOT NULL,
  `tiposolicitud` VARCHAR(45) NOT NULL,
  `descripcionsol` VARCHAR(45) NOT NULL,
  `tecnico2` VARCHAR(45) NOT NULL,
  `responsabledeposito` VARCHAR(45) NOT NULL,
  `actividad` VARCHAR(45) NOT NULL,
  `departamento` VARCHAR(45) NOT NULL,
  `municipio` VARCHAR(45) NOT NULL,
  `diasviaticos` INT NOT NULL,
  `diashotel` INT NOT NULL,
  `asigespeciales` VARCHAR(45) NULL DEFAULT NULL,
  `valorasigespeciales` VARCHAR(45) NULL DEFAULT NULL,
  `estado` TINYINT NOT NULL,
  `usuarios_idusuario` INT NOT NULL,
  `aprobadores_idaprobadores` INT NOT NULL,
  PRIMARY KEY (`idsolicitudes`, `usuarios_idusuario`),
  INDEX `fk_solicitudes_usuarios_idx` (`usuarios_idusuario` ASC) VISIBLE,
  INDEX `fk_solicitudes_aprobadores1_idx` (`aprobadores_idaprobadores` ASC) VISIBLE,
  UNIQUE INDEX `idsolicitudes_UNIQUE` (`idsolicitudes` ASC) VISIBLE,
  CONSTRAINT `fk_solicitudes_usuarios`
    FOREIGN KEY (`usuarios_idusuario`)
    REFERENCES `mydb`.`usuarios` (`idusuarios`),
  CONSTRAINT `fk_solicitudes_aprobadores1`
    FOREIGN KEY (`aprobadores_idaprobadores`)
    REFERENCES `mydb`.`aprobadores` (`idaprobadores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`aprobadores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aprobadores` (
  `idaprobadores` INT NOT NULL,
  `nombreaprobador1` VARCHAR(45) NOT NULL,
  `nombreaprobador2` VARCHAR(45) NOT NULL,
  `fechadeaprobacion1` DATETIME NOT NULL,
  `fechadeaprobacion2` VARCHAR(45) NOT NULL,
  `solicitante` VARCHAR(45) NOT NULL,
  `correoaprob1` VARCHAR(45) NOT NULL,
  `correoaprob2` VARCHAR(45) NOT NULL,
  `solicitudes_idsolicitudes` INT NOT NULL,
  `solicitudes_usuarios_idusuario` INT NOT NULL,
  PRIMARY KEY (`idaprobadores`),
  INDEX `fk_aprobadores_solicitudes1_idx` (`solicitudes_idsolicitudes` ASC, `solicitudes_usuarios_idusuario` ASC) VISIBLE,
  UNIQUE INDEX `idaprobadores_UNIQUE` (`idaprobadores` ASC) VISIBLE,
  CONSTRAINT `fk_aprobadores_solicitudes1`
    FOREIGN KEY (`solicitudes_idsolicitudes` , `solicitudes_usuarios_idusuario`)
    REFERENCES `mydb`.`solicitudes` (`idsolicitudes` , `usuarios_idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
