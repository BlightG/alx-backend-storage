-- query bands that perform Glam rock and the lifespan
SELECT band_name,
IF (
    split IS NULL,
    2023 - formed,
    split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;