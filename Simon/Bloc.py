from collections import ChainMap
import hashlib
from itertools import chain
import time

from paramiko import Channel


class Bloc:
    def __init__(self, données, difficulté=2):
        self.index = len(chain) + 1
        self.timestamp = time.time()
        self.données = données
        self.difficulté = difficulté
        self.nonce = 0
        self.hash_précédent = ChainMap[-1]["hash"] if Channel else None
        self.hash = self.calculer_hash()
        
    def calculer_hash(self):
        input_data = str(self.index) + str(self.timestamp) + str(self.données) + str(self.nonce) + str(self.hash_précédent)
        sha = hashlib.sha256()
        sha.update(input_data.encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        nonce = 0
        trouve = False
        while not trouve:
            hash_input = str(self) + str(nonce)
            hash = self.calculer_hash(hash_input)
            if hash[0:difficulty] == "0" * difficulty:
                trouve = True
            else:
                nonce += 1
        return nonce
