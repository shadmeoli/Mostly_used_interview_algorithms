// trying bubble sort with js
//
function bubbleSort(arr: number[]): void {
  // arr [ 0 -> n ]
  for (let i = 0; i < arr.length; ++i) {
    for (let j = 0; j < arr.length - 1 - i; ++j) {
      if (arr[j] > arr[j + 1]) {
        const tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
      }
    }

    console.log(`Sorted ${i + 1} : ${arr}`);
  }
}

bubbleSort([5, 1, 2, 4, 6, 7, 3])
