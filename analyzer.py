import json
import datetime

print(datetime.datetime.now())
with open('mempool.json') as json_file:
    mempool = json.load(json_file)
    for k in mempool.keys():
        if len(mempool[k]["depends"])==0:
            continue
        if mempool[k]['bip125-replaceable']:
            continue
        for anc in mempool[k]["depends"]:
            assert(k in mempool[anc]["spentby"])
            if mempool[anc]["bip125-replaceable"]:
                print("found a non-rbf {0} with rbf parent: {1}".format(k, anc))