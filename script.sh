/usr/local/bin/bitcoin-cli getrawmempool true > /home/spd/mempool-rbf/mempool.json 2>> /home/spd/mempool-rbf/error.log
/usr/bin/python3 /home/spd/mempool-rbf/checkAncestorRBF.py >> /home/spd/mempool-rbf/rbf.log 2>> /home/spd/mempool-rbf/error.log
/usr/bin/node /home/spd/mempool-rbf/recursivePropertyCheckerTest.js >> /home/spd/mempool-rbf/rbf-js.log 2>> /home/spd/mempool-rbf/error-js.log