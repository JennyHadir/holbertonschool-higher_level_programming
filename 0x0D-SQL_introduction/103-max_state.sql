-- Display max temperature of each state
SELECT state, max(value) FROM temperatures GROUP BY state ORDER BY state ASC;
