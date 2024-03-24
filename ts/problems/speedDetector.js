/**
 * function speed(speed):
 * 	if speed < 70:
 * 		print ok
 * 	otherwise:
 * 		extra_km = speed - 70;
 * 		points = 0
 * 		while extra_km > 5:
 * 			extra_km = extra_km - 5
 * 			points = points +1
 *
 *
 * [result]: if 80 -> 2
 */
function speedDetector(speed) {
	if (speed < 70) {
		return "ok"
	} else if (speed > 70) {
		let extra_km = speed - 70;
		let points = 0;
		while (extra_km > 5 || extra_km === 5) {
			points = points + 1
			extra_km = extra_km - 5;
		}
		return points
	}
}


let results = speedDetector(80) // result 2 points
console.log(results)