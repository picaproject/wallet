from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


def withdraw():

    """ BEP20 BNB Withdraw """

    bscUrl = ""
    web3 = Web3(HTTPProvider(bscUrl))
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)

    fromBscAddress = ""
    fromBscAddress = web3.toChecksumAddress(fromBscAddress)
    fromPrivateKey = ""


    toBscAddress = ""
    amount = 1

    nonce = web3.eth.getTransactionCount(fromBscAddress)

    tx = {
        'chainId': 56,
        'nonce': nonce,
        'to': toBscAddress,
        'value': web3.toWei(amount, "ether"),
        'gas': 70000,
        'gasPrice': web3.eth.gasPrice,
    }

    signed_tx = web3.eth.account.signTransaction(tx, fromPrivateKey)

    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)