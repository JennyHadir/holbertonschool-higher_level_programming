#!/usr/bin/node
/* File system object  */
let url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
request(url + process.argv[2], function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
