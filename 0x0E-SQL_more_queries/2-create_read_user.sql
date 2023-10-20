-- creates the database hbtn_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create the user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'loclahost'
IDENTIFIED BY 'user_0d_2_pwd';

-- grant USAGE privilege on all databases (needed for connection).
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- grant SELECT privilege on the hbtn_0d_2 database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
