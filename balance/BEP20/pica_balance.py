import json
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


def get_balance():
    bscUrl = ""
    web3 = Web3(HTTPProvider(bscUrl))
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)

    bscAddress = ""
    bscAddress = web3.toChecksumAddress(bscAddress)

    picaAbi = ""
    abi = json.dumps(picaAbi)

    picaCA = ""
    picaContract = web3.eth.contract(address=picaCA, abi=abi)

    picaBalance = picaContract.functions.balanceOf(bscAddress).call()