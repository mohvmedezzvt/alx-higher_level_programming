#!/usr/bin/node

const argsNum = process.argv.length - 2;

if (argsNum === 0) {
  console.log('No argument');
} else if (argsNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
