SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstrativos_contabeis d
LEFT JOIN operadoras o ON o.registro_ans = d.reg_ans
WHERE UPPER(d.descricao) LIKE IFNULL(UPPER(CONCAT('%', :descricao, '%')), UPPER('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'))
  AND YEAR(d.data) = :ano
  AND QUARTER(d.data) = :trimestre
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
