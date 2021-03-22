#!/usr/bin/node
let max = 0;
const args = process.argv.map(Number).process.argv.slice(2);
if (process.argv.length > 1) {
  args.sort();
  max = args[args.length - 2];
}
console.log(max);
