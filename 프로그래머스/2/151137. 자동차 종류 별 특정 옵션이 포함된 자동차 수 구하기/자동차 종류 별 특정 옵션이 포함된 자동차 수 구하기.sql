SELECT CAR_TYPE, COUNT(*) AS CARS
FROM (
    SELECT CAR_ID, CAR_TYPE
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE OPTIONS LIKE '%가죽시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%통풍시트%') AS A
GROUP BY A.CAR_TYPE
ORDER BY CAR_TYPE ASC;