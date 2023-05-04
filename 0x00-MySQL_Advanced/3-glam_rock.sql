-- query bands that perform Glam and the lifespan
SELECT band_name,
IF (
    split IS NULL,
    (SELECT YEAR(CURDATE()) AS current_year) - formed,
    split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam%'
ORDER BY lifespan DESC;