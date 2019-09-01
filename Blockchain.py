import hashlib
import time

class Block:

    def __init__(self, timestamp, data, prev_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = prev_hash
      self.hash = self.calc_hash(data)
      self.next=None
      
    def calc_hash(self,data):
        
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')#data will be encoded

      sha.update(hash_str)
      return sha.hexdigest()

class BlockChain:
    
    def __init__(self):
        self.head = None
        
    def add_block(self,data):
        
        timestamp=time.time()
        
        if self.head is None:#first block of the chain
            self.head = Block(timestamp,data,0)
            return
        
        else:    # Move the node to the last
            node = self.head
            while node.next:
                node = node.next
            prev_hash=node.hash
            node.next = Block(timestamp,data,prev_hash)
            return


    def print_blockchain(self):

        if self.head is None:
            print("chain is empty")
        else:
            node=self.head
            if node.next.previous_hash != node.hash:
               printf("hash is different")
               
            else:
                while node:    
                    print(node.timestamp)
                    print(node.data)
                    print(node.previous_hash)
                    node = node.next
		    
def main():

    b1 = BlockChain()


    b1.add_block("first block")
	
    #answer
    """ 1562530542.4521747
        first block
        0"""
	
    b1.add_block("second block")
	
    #answer
    """ 1562530542.4521747
        second block
        2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c"""
	
    b1.add_block("third block")
    #answer
    """ 1562530542.4541702
        third block
        d387a3f3e5c0aebd3847c2dde0a248ddb1fa8f04fe6ff99e9ce7e60fdbcd9c3f"""

    b1.print_blockchain()

    #test case 2
    b2= BlockChain()
    b2.print_blockchain()
    #answer
    #chain is empty

    #test case 3
    b3=BlockChain()

    b3.add_block("head of the block chain")
    #answer
    """ 1563025806.309079
        head of the block chain
        0"""
    b3.add_block("")
    #answer
    """ 1563025806.309079

        76792cc3a488e0888764bdcdc031289be2e3d75eaa1473f3969bb1a9ad03b486"""
    b3.add_block("tail of the block chain")
    #answer
    """ 1563025806.309079
        tail of the block chain
        e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"""
    b3.print_blockchain()
	

	
if __name__ == '__main__':
	main()
    
    
