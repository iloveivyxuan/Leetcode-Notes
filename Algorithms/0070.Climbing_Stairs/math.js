/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  const sqrt5 = Math.sqrt(5);
  const phi = (1 + sqrt5) / 2;
  const psi = (1 - sqrt5) / 2;
  const fibN = (1 / sqrt5) * (Math.pow(phi, n+1) - Math.pow(psi, n+1));

  return Math.round(fibN);
};