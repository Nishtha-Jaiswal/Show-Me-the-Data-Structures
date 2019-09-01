class double_node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRU_Cache(object):
    
    def __init__(self, capacity):
        
        self.front = None #front end of the queue, gets appended with the most recently used value
        self.rear = None  #rear end of the queue, the least recently used value gets shifted to the rear end
        self.hash_map = {}#creating a dictionary to store key:value pair
        self.capacity = capacity #capacity of LRU_cache
        self.current_size = 0
        
        
    def enqueue(self, node):
        #initially no node is present
        if self.front is None:
            self.front = node
            self.rear = node
        #adding nodes to the cache    
        else:
            node.prev = self.front
            self.front.next = node
            self.front = node
        self.current_size += 1
        pass

    def dequeue(self, node):
        if self.front is None:
            return

        # removing arbitrary middle node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # single node is present
        if not node.next and not node.prev:
            self.front = None
            self.rear = None

        #removing the end node
        
        if self.rear == node:
            self.rear = node.next
            self.rear.prev = None
        self.current_size -= 1
        return node
        pass



    def get(self, key):
        
        if key not in self.hash_map: #cache miss
            return -1
        
        node = self.hash_map[key]
        
        if self.front == node: #cache hit
            return node.value
        self.dequeue(node)
        self.enqueue(node)
        return node.value
        pass

    def set(self, key, value):
        if self.capacity <= 0:
            print("cache size is invalid")
            return None
    
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            
            if self.front != node:
                self.dequeue(node)
                self.enqueue(node)
        #when the cache is full, least recently used node is dequeued from the rear end and new node is set at front end        
        else:
            new_node = double_node(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.rear.key]
                self.dequeue(self.rear)
            self.enqueue(new_node)
            self.hash_map[key] = new_node
        pass            


#test case 1    
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


data=our_cache.get(1)       # returns 1
print(data)
data=our_cache.get(2)       # returns 2
print(data)
data=our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(data)

our_cache.set(5, 5) 
our_cache.set(6, 6)

data=our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry    
print(data)

#test case 2    
our_cache = LRU_Cache(0)
our_cache.set(1, 1);   #cache size is invalid
our_cache.set(2, 2);   #cache size is invalid
our_cache.set(3, 3);   #cache size is invalid
our_cache.set(4, 4);   #cache size is invalid


data=our_cache.get(1)       # returns -1 because 1 is not present in the cache
print(data)
data=our_cache.get(2)       # returns -1 because 2 is not present in the cache
print(data)
data=our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(data)

our_cache.set(5, 5)   #cache size is invalid
our_cache.set(6, 6)   #cache size is invalid

data=our_cache.get(3)      # returns -1 because 3 is not present in the cache   
print(data)

#test case 3    
our_cache = LRU_Cache(-1)
our_cache.set(1, 1);   #cache size is invalid
our_cache.set(2, 2);   #cache size is invalid
our_cache.set(3, 3);   #cache size is invalid
our_cache.set(4, 4);   #cache size is invalid


data=our_cache.get(1)       # returns -1 because 1 is not present in the cache
print(data)
data=our_cache.get(2)       # returns -1 because 2 is not present in the cache
print(data)
data=our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(data)

our_cache.set(5, 5)   #cache size is invalid
our_cache.set(6, 6)   #cache size is invalid

data=our_cache.get(3)      # returns -1 because 3 is not present in the cache   
print(data)

