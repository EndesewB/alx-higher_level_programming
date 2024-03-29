#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!Number.isNaN(parseInt(arg1)) && !Number.isNaN(parseInt(arg2))) {
  const num1 = parseInt(arg1);
  const num2 = parseInt(arg2);

  const result = add(num1, num2);
  console.log(result);
} else {
  console.log('NaN');
}
