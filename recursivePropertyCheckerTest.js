#!/usr/bin/env node
var transactionIsNotRBF = require('../react-app/src/util/recursiveRBFChecker.js');
const readline = require('readline');
const fs = require('fs');

const readInterface = readline.createInterface({
    input: fs.createReadStream('rbf.log'),
    console: false
});

let lines = [];

readInterface.on('line', function(line) {
    lines.push(line);
});

readInterface.on('close', function() {
    for (var i=lines.length-1; i>=0; i--) {
        if (lines[i].length!=64) {
            break;
        }
        (async () => {
            try {
                var text = await transactionIsNotRBF.transactionIsNotRBF(lines[i]);
                console.log(text);
            } catch (e) {
                console.log(e);
            }
        })();
    }
});
