SELECT 
    CASE
        WHEN DATE_FORMAT(DIFFERENTIATION_DATE,'%m') IN ('01', '02', '03') THEN '1Q'
        WHEN DATE_FORMAT(DIFFERENTIATION_DATE,'%m') IN ('04', '05', '06') THEN '2Q'
        WHEN DATE_FORMAT(DIFFERENTIATION_DATE,'%m') IN ('07', '08', '09') THEN '3Q'
        WHEN DATE_FORMAT(DIFFERENTIATION_DATE,'%m') IN ('10', '11', '12') THEN '4Q'
END AS QUARTER, COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER;