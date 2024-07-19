/*
Creates mysql database "weather_whisper_db"
Creates mysql user that has acces to the weather_whisper_db
Creates a table "users"
*/

CREATE DATABASE IF NOT EXISTS weather_whisper_db;
CREATE USER IF NOT EXISTS "weather_whisper_dev"@"localhost" IDENTIFIED BY "wwd_pwd";
GRANT ALL PRIVILEGES ON weather_whisper_db.* TO "weather_whisper_dev"@"localhost";
FLUSH PRIVILEGES;

USE weather_whisper_db;


CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	username VARCHAR(100) NOT NULL,
	country_code VARCHAR(10) NOT NULL,
	phone_number VARCHAR(50) NOT NULL,
	country VARCHAR(100) NOT NULL,
	timezone VARCHAR(100) NOT NULL
	city VARCHAR(100) NOT NULL,
	latitude INT(10) NOT NULL,
	longitude INT(10) NOT NULL,
	gender VARCHAR(20) NOT NULL
	);

-- END
