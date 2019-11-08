bitcoin-cli getrawmempool true > mempool.json 2>> error.log
/usr/bin/python3 /home/spd/mempool-rbf/analyzer.py >> rbf.log 2>> error.log