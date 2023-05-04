-- query bands that perform Glam rock and the lifespan
SELECT band_name,
IF (
    split IS NULL,
    (SELECT YEAR(CURDATE()) AS current_year) - formed,
    split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name DESC;