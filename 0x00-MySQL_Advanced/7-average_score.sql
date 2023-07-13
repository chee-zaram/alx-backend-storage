-- SQL script that creates a stored procedure `ComputeAverageScoreForUser`
-- that computes and stores the average score for a student.
-- Note: An average score can be a decimal.

-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
--  user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
COMMENT 'Updates user with given user_id with the average score'
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END $$
DELIMITER ;
