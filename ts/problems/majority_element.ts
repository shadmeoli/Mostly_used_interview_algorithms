// O(1) -> this is my solution
function elemento(arr: number[]): number {
	let count = 0;
	let val = arr[0]

	for (let i = 0; i < arr.length; i++) {
		if (i > 2) {
			val = arr[i]
		} else {
			if (arr[i] === val) {
				count++
			} else (
			count--
			)
		}
	}
	return val
}


/**
 *
 * This is a copied solution
 *
 * // O(1)
function elemento(arr: number[]): number {
	let count = 0;
	let val = arr[0]

	for (let i = 0; i < arr.length; i++) {
		if (count === 0) {
			val = arr[i]
		}
		count+1 ? arr[i] === val : count-1
	}
	return val
}

 *
 */


console.log(elemento([2, 2, 1, 1, 1, 2, 2, 1, 1, 1]))
