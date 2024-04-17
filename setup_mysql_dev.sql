-- Check if the database hbnb_dev_db already exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbnb_dev_db';

-- If it doesn't exist, create it
IF @@rowcount = 0 THEN
  CREATE DATABASE hbnb_dev_db;
END IF;

-- Check if the user hbnb_dev@localhost already exists
SELECT User, Host FROM mysql.user WHERE User = 'hbnb_dev' AND Host = 'localhost';

-- If it doesn't exist, create it with password
IF @@rowcount = 0 THEN
  CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
END IF;

-- Grant all privileges on hbnb_dev_db to hbnb_dev@localhost
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev@localhost
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to ensure immediate effect
FLUSH PRIVILEGES;
