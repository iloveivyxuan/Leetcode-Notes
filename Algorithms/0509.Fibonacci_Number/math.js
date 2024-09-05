/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
  sqrt5 = Math.sqrt(5);
  phi = (1 + sqrt5) / 2;
  phiHat = (1 - sqrt5) / 2;
  fibN = (1 / sqrt5) * (Math.pow(phi, n) - Math.pow(phiHat, n));

  return fibN;
};