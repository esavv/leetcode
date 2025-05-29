# See: https://leetcode.com/problems/lru-cache/
class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):

    # soln #1 on 5/29/2025
    # doubly-linked list + hashmap
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.head = None
        self.tail = None
        
    def useItem(self, key):
        # locate the node in the list
        currNode = self.hashmap[key][1]
        # only bother with updating the node's location if it's not already at the end
        if self.tail != currNode:
            # update the head if the item we're updating is the head
            if self.head == currNode:
                self.head = currNode.next
            # connect the parent & child of the item to one another
            if currNode.prev:
                currNode.prev.next = currNode.next
            if currNode.next:
                currNode.next.prev = currNode.prev
            # move the item from its current position to the end of the list
            self.tail.next = currNode
            currNode.prev = self.tail
            self.tail = currNode

    def get(self, key):
        if key in self.hashmap:
            # mark it as used (move it to end of list)
            self.useItem(key)
            return self.hashmap[key][0]
        return -1        

    def put(self, key, value):
        if key in self.hashmap:
            # update the item's value in the hashmap
            self.hashmap[key][0] = value
            # mark it as used (move it to end of list)
            self.useItem(key)
        else:
            # add the item to the end of the list
            newNode = ListNode(key)
            if self.tail:
                self.tail.next = newNode
                newNode.prev = self.tail
            # handle the case where this is the first item in the cache
            else:
                self.head = newNode
            self.tail = newNode

            # add the item to the hashmap
            self.hashmap[key] = [value, newNode]

            # if we're at capacity
            if len(self.hashmap) > self.capacity:
            #   remove the oldest item from the list
                oldKey = self.head.key
                self.head = self.head.next
                self.head.prev = None
            #   remove that item from the hashmap too
                del self.hashmap[oldKey]
        