-- creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- grant all privileges to the user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- reload the privilege tables and apply the changes immediately.
FLUSH PRIVILEGES;
