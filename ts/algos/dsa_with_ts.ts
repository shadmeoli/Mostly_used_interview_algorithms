/**
 * The floyds algorithm
 */

class Algorithm {
  /**
   *
   * @param nums
   * @returns the duplicate value in the provided array
   */
  public floydsAlgorithm(nums: number[]) {
    let tortoise = nums[0];
    let hare = nums[0];

    while (true) {
      tortoise = nums[tortoise];
      hare = nums[nums[hare]];

      console.log(tortoise, hare);
      if (hare === tortoise) {
        break;
      }
    }

    let pt1 = nums[0];
    let pt2 = tortoise;

    while (pt1 !== pt2) {
      pt1 = nums[pt1];
      pt2 = nums[pt2];
      console.log(pt1, pt2);
    }
    console.log(pt1, pt2, nums);
    return pt1;
  }

  /**
   * This is the impletation of the bubble sort
   * algorithm for sorting through arrays
   * @param nums
   * @returns nums - the sorted array
   */
  public bubbleSort(nums: number[]) {
    console.log(nums);
    for (let i = 0; i < nums.length; i++) {
      for (let j = 0; j < nums.length - i; j++) {
        if (nums[j] > nums[j + 1]) {
          let temp = nums[j];
          nums[j] = nums[j + 1];
          nums[j + 1] = temp;
        }
      }
    }
    return nums;
  }

  /**
   * binary search algorithm
   * @param nums - an array of numbers |  must be a sorted array
   * @param target - the target value to search for
   * @return - the traget, the array of numbers and the index of the target
   */
  public binaySearch(nums: number[], target: number) {
    let low = 0;
    let high = nums.length - 1;

    while (low < high) {
      let mid = low + ((high - low) % 2);
      let val = nums[mid];

      if (val > target) {
        low = mid + 1;
      } else if (val < target) {
        low = mid - 1;
      } else {
        return `${nums}, ${mid}, ${nums.indexOf(val)}`;
      }
    }
  }
}

class Astar {}

let algo = new Algorithm();
// console.log(algo.floydsAlgorithm([1,4,2,3,4,5]))
// console.log(algo.bubbleSort([1,4,2,3,4,5]))
console.log(
  algo.binaySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 11),
);
