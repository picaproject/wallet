from web3 import Web3, HTTPProvider


def create_wallet():
    ethUrl = ""
    web3 = Web3(HTTPProvider(ethUrl))
    password = ""
    ethAddress = web3.personal.newAccount(password)