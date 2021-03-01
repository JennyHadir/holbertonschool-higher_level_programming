-- Lists a specific rows (score and name)
-- Records are shown by order of score
SELECT DISTINCT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
