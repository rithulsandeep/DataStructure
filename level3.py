from level2 import *
from level1 import *
from level0 import *
import heapq
import time


class TimeBasedCache:
    def __init__(self):
        self.cache = {}
        self.expiry_heap = []

    def set(self, key, value, expiryTime):
        expiry_timestamp = time.time() + expiryTime
        self.cache[key] = (value, expiry_timestamp)
        heapq.heappush(self.expiry_heap, (expiry_timestamp, key))
        self._clean_expired()

    def get(self, key):
        self._clean_expired()
        if key in self.cache:
            return self.cache[key][0]
        return None

    def _clean_expired(self):
        current_time = time.time()
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            _, key = heapq.heappop(self.expiry_heap)
            if key in self.cache and self.cache[key][1] <= current_time:
                del self.cache[key]

# Example Usage
if __name__ == "__main__":
    # Doubly Linked List
    dll = DoublyLinkedList()
    dll.insert_head(1)
    dll.insert_tail(2)
    dll.insert_tail(3)
    dll.traverse_forward()  # 1 2 3
    dll.traverse_backward()  # 3 2 1
    
    # MinMax Stack
    stack = MinMaxStack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    print(stack.getMin())  # 2
    print(stack.getMax())  # 5
    stack.pop()
    print(stack.getMin())  # 3
    
    # Interval Merger
    merger = IntervalMerger()
    merger.addInterval(1, 5)
    merger.addInterval(6, 8)
    merger.addInterval(4, 7)
    print(merger.getIntervals())  # [[1, 8]]
    
    # Time-Based Cache
    cache = TimeBasedCache()
    cache.set("a", 100, 2)
    print(cache.get("a"))  # 100
    time.sleep(3)
    print(cache.get("a"))  # None (expired)
