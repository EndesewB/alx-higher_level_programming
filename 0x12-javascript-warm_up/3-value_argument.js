#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else {
  let countArgs = '';
  for (let i = 0; i < args.length; i++) {
    countArgs += args[i];
    if (i !== args.length - 1) {
      countArgs += ' ';
    }
  }
  console.log(countArgs);
}
