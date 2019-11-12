var transactionIsNotRBF = require('../react-app/src/util/recursiveRBFChecker.js');

console.log("starting");
(async () => {
    try {
        var text = await transactionIsNotRBF.transactionIsNotRBF("cf92218cfd2c007ceafb125b1f2c38aa207917b4e6927c7391de0450cb614ced");
        console.log(text);
    } catch (e) {
        console.log(e);
    }
})();