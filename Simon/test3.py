import hashlib
import json
import time


class Bloc:
    def __init__(self, data):
        self.index = None
        self.timestamp = None
        self.data = data
        self.previous_hash = None
        self.hash = None
        self.nonce = None

class Blockchain:
    def __init__(self, difficulty=4): 
        self.difficulty = difficulty
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Bloc("Genesis Block")
        genesis_block.index = 0
        genesis_block.timestamp = time.time()
        genesis_block.previous_hash = None
        genesis_block.nonce = 0
        genesis_block.hash = self.hash_block(genesis_block)
        self.chain.append(genesis_block)

    def hash_block(self, block):
        block_string = json.dumps(block.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, block):
        block.index = len(self.chain)
        block.previous_hash = self.chain[-1].hash
        block.timestamp = time.time()
        block.nonce = 0
        cpt = 0

        while True:
            hash = self.hash_block(block)
            if hash[:self.difficulty] == "0" * self.difficulty:
                block.hash = hash
                self.chain.append(block)
                break
            else:
                cpt += 1 
                print(hash)
                print(cpt)
                print("\n")
                block.nonce += 1

blockchain = Blockchain()
blockchain.add_block(Bloc("Data for Block 2"))
blockchain.add_block(Bloc("Data for Block 3"))

for i, block in enumerate(blockchain.chain):
    print("Block {}".format(i))
    print("Index: {}".format(block.index))
    print("Timestamp: {}".format(block.timestamp))
    print("Data: {}".format(block.data))
    print("Previous Hash: {}".format(block.previous_hash))
    print("Hash: {}".format(block.hash))
    print("Nonce: {}".format(block.nonce))
    print()
