-- Write a script that creates the MySQL server user holberton_user
--      holberton_user should REPLICATION privileges on your MySQL server

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* to 'holberton_user'@'localhost';
