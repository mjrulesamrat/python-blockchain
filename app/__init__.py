from flask import Flask
from .block import BlockChain

app = Flask(__name__)

# Instantiate the Blockchain
blockchain = BlockChain()
