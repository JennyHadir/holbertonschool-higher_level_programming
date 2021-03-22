#!/usr/bin/node
let max = 0;
const args = process.argv.map(Number).process.argv.slice(2, process.argv.length).sort();
if (process.argv.length > 1) {
  max = args[args.length - 2];
}
console.log(max);
