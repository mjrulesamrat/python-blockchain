class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Create new block and adds it to the chain
        pass

    def new_transaction(self):
        # Adds new transaction to the list of current transactions
        pass

    @staticmethod
    def hash(block):
        # hashes a block
        pass

    def last_block(self):
        # Returns last block from the chain
        pass
