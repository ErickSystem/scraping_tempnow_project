CREATE TABLE `country` (
    `id`   INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(80) NOT NULL,
    `code` CHAR(2) NOT NULL,

    CONSTRAINT `country_pkey` PRIMARY KEY (`id` ASC)
);

CREATE TABLE `region` (
    `id`               INT NOT NULL AUTO_INCREMENT,
    `name`             VARCHAR(50) NOT NULL,
    `code`             CHAR(2) NOT NULL,
    `default_timezone` VARCHAR(50) NOT NULL,
    `country_id`       INT NOT NULL,

    CONSTRAINT `region_pkey` PRIMARY KEY (`id` ASC),
    CONSTRAINT `region_country_id_fkey` FOREIGN KEY (`country_id`) REFERENCES `country`(`id`)
);

CREATE TABLE `locality` (
    `id`        INT NOT NULL AUTO_INCREMENT,
    `name`      VARCHAR(100) NOT NULL,
    `region_id` INT NOT NULL,

    CONSTRAINT `locality_pkey` PRIMARY KEY (`id` ASC),
    CONSTRAINT `locality_region_id_fkey` FOREIGN KEY (`region_id`) REFERENCES `region`(`id`)
);

CREATE TABLE `weather_forecasting_hour`
(
 `id`                       INT NOT NULL AUTO_INCREMENT,
 `atmospheric_pressure`     INT NOT NULL ,
 `wind`                     INT NOT NULL ,
 `temp`                     INT NOT NULL ,
 `relative_humidity`        INT NOT NULL ,
 `last_update`              TEXT NULL ,
 `weather`                  TEXT NOT NULL ,
 `locality_id`              INT NOT NULL ,
 `date_time`                DATETIME NOT NULL ,

 CONSTRAINT `weather_forecasting_hour_pkey` PRIMARY KEY (`id` ASC),
 CONSTRAINT `weather_forecasting_hour_locality_id_fkey` FOREIGN KEY (`locality_id`)  REFERENCES `locality`(`id`)
);

CREATE TABLE `weather_forecasting_day`
(
 `id`                INT NOT NULL AUTO_INCREMENT,
 `weather`           TEXT NOT NULL ,
 `precipitation`     INT NOT NULL ,
 `date`              DATE NOT NULL ,
 `max`               INT NOT NULL ,
 `min`               INT NOT NULL ,
 `locality_id`       INT NOT NULL ,
 `lag`               INT NOT NULL ,

 CONSTRAINT `weather_forecasting_day_pkey` PRIMARY KEY (`id` ASC),
 CONSTRAINT `weather_forecasting_day_locality_id_fkey` FOREIGN KEY (`locality_id`)  REFERENCES `locality`(`id`)
);

ALTER TABLE `locality` ADD CONSTRAINT `locality_name_region_id_akey` UNIQUE (`region_id`, `name` ASC);