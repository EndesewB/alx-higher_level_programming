#!/usr/bin/node

const args = process.argv.slice(2);
let counter = 0;

while (args[counter] !== undefined) {
  counter++;
}

if (counter === 0) {
  console.log('No argument');
} else {
  let concatenateArgs = '';
  for (let i = 0; i < counter; i++) {
    concatenateArgs += args[i];
    if (i !== counter - 1) {
      concatenateArgs += ' ';
    }
  }
  console.log(concatenateArgs);
}
