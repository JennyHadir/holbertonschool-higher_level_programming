#!/usr/bin/node
/* File system object  */
const fs = require('fs');

/* Read File */
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
