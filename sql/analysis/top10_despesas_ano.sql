SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstrativos_contabeis d
LEFT JOIN operadoras o ON o.registro_ans = d.reg_ans
WHERE UPPER(d.descricao) = IFNULL(UPPER(:descricao), UPPER('EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS NA MODALIDADE DE PAGAMENTO POR PROCEDIMENTO'))
  AND YEAR(d.data) = :ano
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
