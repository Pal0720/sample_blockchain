# Creating a tiny blockchain in 50 lines of python.

import hashlib
import datetime

#creating structure of the block
class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash))
        return sha.hexdigest()


#now, create the chain
# defining a function for creating the genesis block

def create_genesis_block():
    # manually create a block since genesis block is a special block
    # with index 0 and arbitrary previous hash
    return Block(0, datetime.datetime.now(), "Genesis block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Hey, I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


#create the blockchain
# it is just a simple python list

blockchain = [create_genesis_block()]
previous_block = blockchain[0] # assign the initial block to the previous block

num_of_blocks = 20 # building a small chain

for i in range(0, num_of_blocks):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    #Logging
    print("Block #{} has been added to blockchain".format(block_to_add.index))
    print("Hash : {}".format(block_to_add.hash))
