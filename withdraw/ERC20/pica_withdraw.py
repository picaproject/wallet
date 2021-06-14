from web3 import Web3, HTTPProvider


def withdraw():

    """ ERC20 PICA Withdraw"""

    ethUrl = ""
    web3 = Web3(HTTPProvider(ethUrl))

    fromEthAddress = ""
    fromEthAddress = web3.toChecksumAddress(fromEthAddress)
    fromEthPassword = ""

    toEthAddress = ""
    toEthAddress = web3.toChecksumAddress(toEthAddress)

    picaCA = ""
    picaAbi = ""

    picaContract = web3.eth.contract(picaCA, abi=picaAbi)

    amount = 1

    unlockFromEthAddress = web3.personal.unlockAccount(fromEthAddress, fromEthPassword)

    tx_hash = picaContract.functions.transfer(
        toEthAddress, amount).transact(
        {
            'from': fromEthAddress
        }
    )

    tx_receipt = web3.eth.getTransaction(tx_hash)

    lockFromEthAddress = web3.personal.lockAccount(fromEthAddress)