#!/usr/bin/node
const array = process.argv.slice(2); //The process.argv property is an array that contains the command-line arguments passed to the Node.js process.
//We slice the array starting from the third item to get only the arguments passed to our script.
if (array[0] === undefined && array[1] === undefined) {
  console.log('undefined is undefined');
} else if (array[0] !== undefined && array[1] !== undefined) {
  console.log(array[0] + ' is ' + array[1]);
} else if (array[0] !== undefined && array[1] === undefined) {
  console.log(array[0] + ' is undefined');
} else if (array[0] === undefined && array[1] !== undefined) {
  console.log('undefined is ' + array[1]);
}
