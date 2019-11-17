import json
import datetime

import simplejson as json
from IPython import embed
import requests

with open("/home/spd/.bitcoin/.cookie", "r") as creds:
    cookie = creds.read()

NODE_URL = "http://127.0.0.1:8332"
NODE_USER = cookie.split(":")[0]
NODE_PASSWORD = cookie.split(":")[1]


def rpc(method, params=[]):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    response = requests.post(NODE_URL, auth=(
        NODE_USER, NODE_PASSWORD), data=payload).json()
    if response['error'] is not None:
        raise Exception(response['error'])
    else:
        return response['result']
    return


def getTx(txid):
    resp = rpc('getrawtransaction', [txid])
    return rpc('decoderawtransaction', [resp])


RBF_ALLOWED_INCLUSIVE = 4294967294


def signalsRBF(tx):
    return any(map(lambda input: input["sequence"] <= RBF_ALLOWED_INCLUSIVE, tx['vin']))


print(datetime.datetime.now())
with open('mempool.json') as json_file:
    mempool = json.load(json_file)
    for k in mempool.keys():
        if len(mempool[k]["depends"]) == 0:
            continue
        if not mempool[k]['bip125-replaceable']:
            continue
        tx = getTx(k)
        if signalsRBF(tx):
            continue
        for anc in mempool[k]["depends"]:
            ancTx = getTx(anc)
            if signalsRBF(ancTx):
                print(k)
