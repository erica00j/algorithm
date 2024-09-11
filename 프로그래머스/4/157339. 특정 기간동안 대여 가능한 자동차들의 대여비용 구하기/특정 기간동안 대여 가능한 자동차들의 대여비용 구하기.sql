SELECT CAR_ID, A.CAR_TYPE, ROUND((30*DAILY_FEE*(100-DISCOUNT_RATE)/100)) AS FEE
FROM (
    SELECT CAR_ID, CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_ID NOT IN (SELECT CAR_ID
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01')
    AND CAR_TYPE IN ('세단','SUV')) AS A
JOIN (SELECT CAR_TYPE,DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE='30일 이상') AS B
ON A.CAR_TYPE=B.CAR_TYPE
HAVING FEE>=500000 AND FEE<2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;