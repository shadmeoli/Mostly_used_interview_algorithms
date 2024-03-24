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
    return "ok";
  } else if (speed > 70) {
    let extra_km = speed - 70;
    let points = 0;
    while (extra_km > 5 || extra_km === 5) {
      points = points + 1;
      extra_km = extra_km - 5;
    }
    return points;
  }
}

// let results = speedDetector(80) // result 2 points
// console.log(results)

/**
 * Write a program whose major task is to calculate
 * the Net Salary by  getting inputs basic salary and
 * benefits.
 * Calculate payee, NHIF, NSSF, gross and net
 *
 */
function getNetSalary(basic, benefits) {
  const NHIF_RATES = {
    5999: 150,
    7999: 300,
    11999: 400,
    14999: 500,
    19999: 600,
    24999: 750,
    29999: 850,
    34999: 900,
    39999: 950,
    44999: 1000,
    49999: 1100,
    59999: 1200,
    69999: 1300,
    79999: 1400,
    89999: 1500,
    99999: 1600,
    100000: 1700,
  };

  const THE_RATES = [
    5999, 7999, 11999, 14999, 19999, 24999, 29999, 34999, 39999, 44999, 49999,
    59999, 69999, 79999, 89999, 99999, 100000,
  ];

  let NHIF_AMOUNT = 0;

  for (let i = 0; i < THE_RATES.length; i++) {
    if (basic <= THE_RATES[i]) {
      NHIF_AMOUNT = NHIF_RATES[THE_RATES[i]];
      break;
    } else if (basic > 100000) {
      NHIF_AMOUNT = 1700;
    }
  }

  const PAYEE_RATES = {
    24000: 10.0,
    32333: 25.0,
    500000: 30.0,
    800000: 32.5,
    800001: 35.0,
  };

  let payee_amount = 0;

  for (const rate of Object.keys(PAYEE_RATES)) {
    if (basic <= rate) {
      payee_amount = PAYEE_RATES[rate];
      break;
    }
  }

  const NSSF_RATES = 0.06; // percentage as decimal
  const NSSF_AMOUNT = basic * NSSF_RATES; // amount individual should pay

  let net_salary = basic - NHIF_AMOUNT - NSSF_AMOUNT - payee_amount;

  return net_salary;
}

console.log(getNetSalary(90000));
