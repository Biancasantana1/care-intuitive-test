LOAD DATA INFILE :full_path
INTO TABLE demonstrativos_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = IF(LOCATE('/', TRIM(@data)) > 0,
            STR_TO_DATE(TRIM(@data), '%d/%m/%Y'),
            STR_TO_DATE(TRIM(@data), '%Y-%m-%d')),
  reg_ans = NULLIF(TRIM(@reg_ans), ''),
  vl_saldo_inicial = CAST(REPLACE(TRIM(@vl_saldo_inicial), ',', '.') AS DECIMAL(18,2)),
  vl_saldo_final = CAST(REPLACE(TRIM(@vl_saldo_final), ',', '.') AS DECIMAL(18,2));
