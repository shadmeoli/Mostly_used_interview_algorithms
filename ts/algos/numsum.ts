/**
 * Write a function that counts the number of times that a
 * value has been repeated in a range of values.
 *
 *
 *
 * */

function finder(range: number, target: number): number {
  let count: number = 0;

  for (let i = 0; i < range + 1; i++) {
    i.toString();
    if (`${i}`.includes(target.toString())) {
      count += 1;
    }
  }

  return count;
}

console.log(finder(100, 9));
