-- Cria o banco de dados se não existir
CREATE DATABASE IF NOT EXISTS careintuitive CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Cria o usuário root (caso não exista) com mysql_native_password e garante todos os privilégios
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root123';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

-- Concede permissão para usar LOAD DATA INFILE
GRANT FILE ON *.* TO 'root'@'%';

-- Aplica as alterações
FLUSH PRIVILEGES;
