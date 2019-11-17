import json
import datetime
from IPython import embed

print(datetime.datetime.now())
counts = [0, 0, 0]
with open('mempool.json') as json_file:
    mempool = json.load(json_file)
    for k in mempool.keys():
        if len(mempool[k]["depends"]) == 0:
            counts[0] += 1
            continue
        if mempool[k]['bip125-replaceable']:
            counts[1] += 1
            continue
        print(k)
        for anc in mempool[k]["depends"]:
            assert(k in mempool[anc]["spentby"])
            if mempool[anc]["bip125-replaceable"]:
                print(k)
print(counts)
