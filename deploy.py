# Author: Bon Filey (bonfiley@gmail.com)
# Copyright 2018 Bromley Labs Inc.

from hexbytes import HexBytes
import sys
from utils import *
import utils
from web3.auto import w3

GAS_PRICE = int(2.5*1e9) 
GAS = int(4*1e6)
PATH = '/home/puneet/crypto/zksnark/contracts/target' 

logger = None

def main():
    if len(sys.argv) != 2:
        print('Usage: python deploy.py  <contract_name>')
        exit(0)
    global logger

    logger = init_logger('DEPLOY', '/tmp/stride.log')
    utils.logger = logger 
    contract_name = sys.argv[1] 
    deploy(w3, contract_name, PATH, w3.eth.accounts[0], GAS, GAS_PRICE)

if __name__== '__main__':
    main()
