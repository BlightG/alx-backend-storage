-- creates a stored procedure AddBonus that adds a new correction for a studen
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    INSERT INTO `corrections`(`user_id`, `project_id`, `score`)
    SELECT user_id, projects.id, score
    FROM projects
    JOIN corrections ON projects.id = project_id
    WHERE projects.name = project_name;
END //
DELIMITER ;