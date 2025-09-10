/**
 * The digits 1,2,3,4,5 can be
 * arraged to form many different
 * 5-digit positive intergers
 * with 5 distinct digits.
 * In how many such intergers
 * is the digit 1 to the left
 * of the digit 2?
 * Two such integers to include
 * are :
 * 	- 14,352
 * 	- 51,234
 */

function permute(nums: number[]): number[][] {
	let results: number[][] = [];

    if (nums.length === 1) {
        return [nums.slice()];
    }

    for (let i = 0; i < nums.length; i++) {
        const n = nums.splice(0, 1)[0];
        const perms = permute(nums.slice());
        for (const perm of perms) {
            perm.push(n);
        }
        results.push(...perms);
        nums.push(n);
    }

    return results;
}
