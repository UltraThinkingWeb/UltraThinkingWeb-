import hashlib
import time
import random
import asyncio

# ✅ Klasa e Bllokut Blockchain
class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.mine_block()

    def mine_block(self, difficulty=4):
        """ Simulimi i proof-of-work me hash SHA-256 """
        while True:
            self.nonce += 1
            block_hash = self.calculate_hash()
            if block_hash[:difficulty] == "0" * difficulty:
                return block_hash

    def calculate_hash(self):
        """ Llogarit hash-in e bllokut """
        block_string = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}{self.nonce}"
