#!/usr/bin/node
/* Computes the number of task completed by user id */
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};
    for (const task of todos) {
      if (task.completed) {
        if (task.userId in completed) {
          completed[task.userId] += 1;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
  console.log(error);
});
