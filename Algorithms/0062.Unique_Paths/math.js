/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
  let numerator = 1;
  let denominator = 1;
  let total = m + n - 2;
  let choose = m - 1;

  for (let i = 0; i < choose; i++) {
      numerator *= total - i;
  }
  for (let i = 0; i < choose; i++) {
      denominator *= choose - i;
  }

  return numerator / denominator;
};