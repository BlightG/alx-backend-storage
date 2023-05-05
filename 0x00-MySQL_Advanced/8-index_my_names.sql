-- indexed a list
-- ALTER TABLE names
-- ADD COLUMN first_letter VARCHAR(1) AS (SUBSTRING(name, 1, 1)) STORED;
-- CREATE INDEX idx_name_first ON names (first_letter);
CREATE INDEX idx_name_first ON names (SUBSTR(name, 1, 1));