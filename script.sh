/usr/local/bin/bitcoin-cli getrawmempool true > /home/spd/mempool-rbf/mempool.json 2>> /home/spd/mempool-rbf/error.log
/usr/bin/python3 /home/spd/mempool-rbf/analyzer.py >> /home/spd/mempool-rbf/rbf.log 2>> /home/spd/mempool-rbf/error.log