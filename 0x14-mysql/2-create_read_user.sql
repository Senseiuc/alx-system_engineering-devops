	-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
--      user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
--      The user_0d_2 password should be set to user_0d_2_pwd
--      If the database hbtn_0d_2 already exists, your script should not fail
--      If the user user_0d_2 already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS tyrell_corp;
GRANT SELECT ON `tyrell_corp`.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (id INT, name VARCHAR(256) NOT NULL);
use tyrell_corp;
INSERT INTO nexus6 (id, name) VALUES (1, 'Best School');
