-- a trggier that resets value of valid_email if email changes
DELIMITER //
CREATE TRIGGER email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN 
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;//
DELIMITER ;