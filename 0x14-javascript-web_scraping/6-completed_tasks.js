#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const tasks = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (tasks[task.userId] === undefined) {
        tasks[task.userId] = 0;
      }
      tasks[task.userId]++;
    }
  }
  console.log(tasks);
});
