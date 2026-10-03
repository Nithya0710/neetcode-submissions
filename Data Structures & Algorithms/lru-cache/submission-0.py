class ListNode:
    def __init__(self, key, value):
        self.key=key
        self.val=value
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.head=ListNode(0, 0)
        self.tail=ListNode(0, 0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def insert(self, node):
        prevNode=self.tail.prev
        prevNode.next=node
        node.prev=prevNode
        node.next=self.tail
        self.tail.prev=node

    def remove(self, node):
        nextNode=node.next
        prevNode=node.prev
        prevNode.next=nextNode
        nextNode.prev=prevNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=ListNode(key, value)
        self.insert(node)
        self.cache[key]=node
        if len(self.cache)>self.cap:
            lru=self.head.next
            self.remove(lru)
            del self.cache[lru.key]
