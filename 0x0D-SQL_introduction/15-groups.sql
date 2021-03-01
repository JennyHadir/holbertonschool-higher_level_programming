-- List the number of records with the same score in the table
SELECT score, COUNT(*) as number from second_table GROUP BY score ORDER BY number DESC;
