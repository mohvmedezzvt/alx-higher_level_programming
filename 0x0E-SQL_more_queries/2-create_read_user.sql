-- creates the database hbtn_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create the user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- grant SELECT privilege on the hbtn_0d_2 database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- flush privileges to apply the changes.
FLUSH PRIVILEGES;
