from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


def create_wallet():
    bscUrl = ""
    web3 = Web3(HTTPProvider(bscUrl))
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)

    password = ""
    bscAccount = web3.eth.account.create(password)

    bscAddress = bscAccount.address
    privateKey = bscAccount.privateKey