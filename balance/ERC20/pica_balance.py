from web3 import Web3, HTTPProvider


def get_balance():
    ethUrl = ""
    web3 = Web3(HTTPProvider(ethUrl))

    ethAddress = ""
    ethAddress = web3.toChecksumAddress(ethAddress)

    picaCA = ""
    picaAbi = ""

    picaContract = web3.eth.contract(picaCA, abi=picaAbi)
    picaBalance = picaContract.functions.balanceOf(ethAddress).call()