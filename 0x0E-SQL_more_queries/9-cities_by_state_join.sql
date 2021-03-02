-- Display cities in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id;
