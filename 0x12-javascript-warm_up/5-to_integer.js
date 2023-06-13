#!/usr/bin/node

const arg = process.argv[2];
const parsedNumber = parseFloat(arg);

if (Number.isInteger(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
