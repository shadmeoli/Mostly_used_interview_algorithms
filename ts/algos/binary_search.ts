function search(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low < high) {
    let mid = low + ((high - low) % 2);
    let val = arr[mid];

    if (val > target) {
      low = mid + 1;
    } else if (val < target) {
      low = mid - 1;
    } else {
      return `${val}, ${mid}`;
    }
  }
}

console.log(search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6));
