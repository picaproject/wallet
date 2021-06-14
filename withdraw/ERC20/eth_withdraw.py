from web3 import Web3, HTTPProvider


def withdraw():

    """ ERC20 ETH Withdraw """

    ethUrl = ""
    web3 = Web3(HTTPProvider(ethUrl))

    fromEthAddress = ""
    fromEthAddress = web3.toChecksumAddress(fromEthAddress)
    fromEthPassword = ""

    toEthAddress = ""
    toEthAddress = web3.toChecksumAddress(toEthAddress)

    amount = 1

    unlockFromEthAddress = web3.personal.unlockAccount(fromEthAddress, fromEthPassword)

    tx_hash = web3.eth.sendTransaction({
        'from': fromEthAddress,
         'to': toEthAddress,
         'value': web3.toWei(amount, "ether")
        }
    )

    tx_receipt = web3.eth.getTransaction(tx_hash)

    lockFromEthAddress = web3.personal.lockAccount(fromEthAddress)