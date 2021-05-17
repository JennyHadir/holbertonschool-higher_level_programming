#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  let count = 0;
  if (error) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
