CREATE TABLE IF NOT EXISTS demonstrativos_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans VARCHAR(10),
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(18,2),
    vl_saldo_final DECIMAL(18,2)
);