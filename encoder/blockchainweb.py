from web3 import Web3
import json
import datetime
pubickey = "0x72d94c339AEa83b51fD697A5878cc646Ac02Eec5"

def getmsg(con):
    s=con.functions.getmess().call()
    return s

def createmsg(w,c,d):


    tx= c.functions.message_production(d['f'],d['to'],d["name"],d["eanid"],d["num"],d["time"],d["producer"],d["price"],d["outprice"]).transact({'from':w.eth.accounts[0],"chainId":666})
    sta=w.eth.waitForTransactionReceipt(tx)

    return sta


if __name__ == '__main__':

    # time=datetime.datetime.now()
    # s=time.strftime('%Y-%m-%d %H:%M')
    # print(type(s))
    # a=123.4
    # print(type(str(a)))
    contractaddress = "0x0d327724A2C85296F3d6BAaE5f5280e08bAC7013"

    provide0key = "owner"
    url = 'http://localhost:8545'

    w3 = Web3(Web3.HTTPProvider(url))
    print(w3.eth.blockNumber)
    print(w3.eth.getTransactionCount(contractaddress))
    print(w3.geth.personal.unlockAccount(w3.eth.accounts[0], "owner"))
    print(w3.geth.personal.newAccount('10086'))

    print(w3.eth.accounts)
    # address="0xef82623213bec30d7de49e61dee6440f4a8e7d3b"
    # s=w3.toChecksumAddress(address)
    #
    # abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"allInfo","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"eanid","type":"string"},{"internalType":"address","name":"source","type":"address"},{"internalType":"string","name":"going","type":"string"},{"internalType":"string","name":"producer","type":"string"},{"internalType":"string","name":"time","type":"string"},{"internalType":"uint256","name":"num","type":"uint256"},{"internalType":"string","name":"price","type":"string"},{"internalType":"string","name":"outprice","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getmess","outputs":[{"components":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"eanid","type":"string"},{"internalType":"address","name":"source","type":"address"},{"internalType":"string","name":"going","type":"string"},{"internalType":"string","name":"producer","type":"string"},{"internalType":"string","name":"time","type":"string"},{"internalType":"uint256","name":"num","type":"uint256"},{"internalType":"string","name":"price","type":"string"},{"internalType":"string","name":"outprice","type":"string"}],"internalType":"struct Goodsystem.Message[]","name":"","type":"tuple[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"message","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"eanid","type":"string"},{"internalType":"address","name":"source","type":"address"},{"internalType":"string","name":"going","type":"string"},{"internalType":"string","name":"producer","type":"string"},{"internalType":"string","name":"time","type":"string"},{"internalType":"uint256","name":"num","type":"uint256"},{"internalType":"string","name":"price","type":"string"},{"internalType":"string","name":"outprice","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"s","type":"address"},{"internalType":"string","name":"going","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"eanid","type":"string"},{"internalType":"uint256","name":"num","type":"uint256"},{"internalType":"string","name":"time","type":"string"},{"internalType":"string","name":"producer","type":"string"},{"internalType":"string","name":"price","type":"string"},{"internalType":"string","name":"outprice","type":"string"}],"name":"message_production","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
    # contract=w3.eth.contract(address=contractaddress,abi=abi)
    #
    #
    # d={'f':s,'to':'12',"name":"test","eanid":'234324',"num":4,"time":"2022-3-3","producer":'wwww',"price":'132',"outprice":'0'}
    # print(createmsg(w3,contract,d))
    #
    # a=getmsg(contract)
    # print(a)