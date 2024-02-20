/**
 *
 * @param (number) thresh
 * @returns number
 */
function findingNines(thresh: number, value: number): number {
  let results: number[] = [];
  for (let val = 0; val < thresh; val++) {
    if (
      val.toString().endsWith(value.toString()) ||
      val.toString().includes(value.toString())
    ) {
      results.push(val);
    }
  }
  return results.length;
}

console.log("");
