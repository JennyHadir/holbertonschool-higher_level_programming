-- Display max temperature of each state
SELECT state, max(value) 'max_temp' FROM temperatures GROUP BY state ORDER BY state ASC;
