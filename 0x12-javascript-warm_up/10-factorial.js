#!/usr/bin/node
const a = process.argv[2];
function factoriel (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return (a * factoriel(a - 1));
  }
}
console.log(factoriel(a));
