#!/usr/bin/node
exports.callMeMoby = function (x, functionToUse) {
  for (let i = 0; i < x; i++) {
    functionToUse();
  }
};
