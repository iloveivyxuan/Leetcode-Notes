/**
 * @param {string} currentState
 * @return {string[]}
 */
var generatePossibleNextMoves = function(currentState) {
  let rv = [];

  for (let i = 0; i < currentState.length - 1; i++) {
      if (currentState[i] === '+' && currentState[i+1] === '+') {
          rv.push(currentState.substring(0, i) + '--' + currentState.substring(i+2, currentState.length));
      }
  }

  return rv;
};