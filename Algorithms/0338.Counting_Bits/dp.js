/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
  let dp = [];
  dp[0] = 0;

  for (let m = 0; 2**m <= n; m++) {
      for (let l = 0; l < 2**m && 2**m + l <=n; l++) {
          dp[2**m + l] = 1 + dp[l];
      }
  }

  return dp;
};
