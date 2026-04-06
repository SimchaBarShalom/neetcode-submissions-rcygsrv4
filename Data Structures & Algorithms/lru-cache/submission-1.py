class Node:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
    
    def insert(self,node):
        prev_node=self.tail.prev
        next_node=self.tail
        node.prev=prev_node
        node.next=next_node
        prev_node.next=node
        next_node.prev=node

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head      

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.capacity:
            node=self.head.next
            self.remove(node)
            del self.cache[node.key]
        

        

        
