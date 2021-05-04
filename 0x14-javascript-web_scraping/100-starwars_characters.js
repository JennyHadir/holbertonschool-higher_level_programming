#!/usr/bin/node
/* Display all characters from star wars api */
const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
request(url + process.argv[2], function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log(error);
  }
});
