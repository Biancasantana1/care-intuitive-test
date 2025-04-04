LOAD DATA INFILE :full_path
INTO TABLE operadoras
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
  @registro_ans,
  cnpj,
  razao_social,
  nome_fantasia,
  modalidade,
  logradouro,
  numero,
  complemento,
  bairro,
  cidade,
  @uf,
  cep,
  ddd,
  telefone,
  fax,
  endereco_eletronico,
  representante,
  cargo_representante,
  regiao_de_comercializacao,
  @data_registro_ans,
  @dummy
)
SET
  registro_ans = TRIM(@registro_ans),
  uf = TRIM(@uf),
  data_registro_ans = STR_TO_DATE(TRIM(@data_registro_ans), '%Y-%m-%d');
