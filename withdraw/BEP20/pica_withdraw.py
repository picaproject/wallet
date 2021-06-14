import json
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


def withdraw():

    """ BEP20 PICA Withdraw """

    bscUrl = ""
    web3 = Web3(HTTPProvider(bscUrl))
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)

    picaAbi = ""
    abi = json.dumps(picaAbi)

    picaCA = ""
    picaContract = web3.eth.contract(address=picaCA, abi=abi)

    fromBscAddress = ""
    fromBscAddress = web3.toChecksumAddress(fromBscAddress)
    fromPrivateKey = ""

    toBscAddress = ""
    amount = 1

    tx = picaContract.functions.transfer(
        toBscAddress, amount).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'nonce': web3.eth.getTransactionCount(fromBscAddress)
    })

    signed_txn = web3.eth.account.signTransaction(tx, fromPrivateKey)

    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)