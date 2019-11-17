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


def my_criterion(tx):
    return single_in_and_out(tx) and input_segwit(tx) and output_segwit(tx)


def input_segwit(tx):
    return len(tx['vin'][0].get('txinwitness', [])) > 0


def output_segwit(tx):
    return tx['vout'][0]['scriptPubKey']['addresses'][0][:4] == 'bc1q'


def mine(tx):
    try:
        return tx['vout'][0]['scriptPubKey']['addresses'][0][:4] == 'bc1q'
    except:
        return False


def single_in_and_out(tx):
    return len(tx['vin']) == 1 and len(tx['vout']) == 1


print(datetime.datetime.now())
with open('mempool.json') as json_file:
    mempool = json.load(json_file)
    count = 0
    for k in mempool.keys():
        resp = rpc('getrawtransaction', [k])
        tx = rpc('decoderawtransaction', [resp])
        if my_criterion(tx):
            print(k)
            count += 1
    print("{0} txs fulfilled criterion".format(count))
