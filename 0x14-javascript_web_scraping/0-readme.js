#!/usr/bin/node
/* File system object  */
const fs = require('fs');

/* Read File */
fs.readFile(process.argv[2], 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
