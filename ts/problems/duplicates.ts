/**
 * This is a simple function to find
 * duplicates in an array
 */
function duplicates(arr: number[]): number[] {
  let dups: number[] = [];
  let fallback = new Set();

  for (let i = 0; i < arr.length; i++) {
    if (fallback.has(arr[i])) {
      dups.push(arr[i]);
    } else {
      fallback.add(arr[i]);
    }
  }
  return dups;
}

console.log(duplicates([1, 2, 3, 2, 4, 3]));
