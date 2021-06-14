from web3 import Web3, HTTPProvider


def get_balance():
    ethUrl = ""
    web3 = Web3(HTTPProvider(ethUrl))

    ethAddress = ""
    ethAddress = web3.toChecksumAddress(ethAddress)

    ethBalance = web3.eth.getBalance(ethAddress)  # 내 잔액조회
    ethBalance = web3.fromWei(ethBalance, "ether")