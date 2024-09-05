/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
  if (n === 2) return 1;
  if (n === 3) return 2;
  if (n === 4) return 4;

  if (n % 3 === 0) {
      return Math.pow(3, n/3)
  } else if (n % 3 === 1) {
      return Math.pow(3, Math.floor(n-4)/3) * 4
  } else {
      return Math.pow(3, Math.floor(n/3)) * 2
  }
};