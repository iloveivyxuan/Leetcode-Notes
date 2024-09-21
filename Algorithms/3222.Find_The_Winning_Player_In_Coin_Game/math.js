/**
 * @param {number} x
 * @param {number} y
 * @return {string}
 */
var losingPlayer = function(x, y) {
  if (Math.min(x, Math.floor(y / 4)) % 2 === 0) {
      return 'Bob'
  } else {
      return 'Alice'
  }
};