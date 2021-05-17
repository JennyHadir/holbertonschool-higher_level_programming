#!/usr/bin/node
let max = 0;
const args = process.argv.slice(2);
if (process.argv.length > 3) {
  args.sort((a, b) => a - b);
  max = args[args.length - 2];
}
console.log(max);
