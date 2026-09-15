-- 1. Annual UK passenger totals
SELECT
    strftime('%Y', date) AS year,
    SUM(total_passengers) AS total_passengers
FROM aviation
WHERE airport_group != 'Non UK Reporting Airports'
GROUP BY year
ORDER BY year;


-- 2. Top 10 UK airports by passenger traffic in 2025
SELECT
    airport,
    SUM(total_passengers) AS total_passengers
FROM aviation
WHERE
    airport_group != 'Non UK Reporting Airports'
    AND strftime('%Y', date) = '2025'
GROUP BY airport
ORDER BY total_passengers DESC
LIMIT 10;


-- 3. Categorise airport traffic using CASE
SELECT
    date,
    airport,
    total_passengers,
    CASE
        WHEN total_passengers >= 1000000 THEN 'High traffic'
        ELSE 'Lower traffic'
    END AS traffic_category
FROM aviation
WHERE airport_group != 'Non UK Reporting Airports'
LIMIT 10;


-- 4. Compare major airport passenger traffic: 2019 vs 2025
WITH airport_totals AS (
    SELECT
        airport,
        SUM(CASE
            WHEN strftime('%Y', date) = '2019'
            THEN total_passengers
            ELSE 0
        END) AS passengers_2019,

        SUM(CASE
            WHEN strftime('%Y', date) = '2025'
            THEN total_passengers
            ELSE 0
        END) AS passengers_2025

    FROM aviation
    WHERE airport_group != 'Non UK Reporting Airports'
    GROUP BY airport
)

SELECT
    airport,
    passengers_2019,
    passengers_2025,
    ROUND(
        ((passengers_2025 - passengers_2019) * 100.0)
        / passengers_2019,
        2
    ) AS percentage_change
FROM airport_totals
WHERE passengers_2019 >= 5000000
ORDER BY percentage_change DESC;
