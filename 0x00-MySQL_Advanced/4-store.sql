-- a trggier that manages the inventory
DELIMITER //
CREATE TRIGGER STORE AFTER INSERT ON orders
FOR EACH ROW
BEGIN 
    UPDATE items
    SET items.quantity = items.quantity - NEW.number
    WHERE items.name = NEW.item_name;
END//
DELIMITER ;