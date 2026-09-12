#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Node:
    __slots__ = ('key', 'value', 'prev', 'next')
    
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # 哨兵节点：head <-> tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
        else:
            node = Node(key, value)
            self.cache[key] = node
        self.add_to_head(node)

        if len(self.cache) > self.capacity:
            removed = self.tail.prev
            del self.cache[removed.key]
            self.remove(removed)

    # 1. 从链表中删除某个节点 (O(1))
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 2. 将节点插入到最前面（紧跟在伪头后面）(O(1))
    def add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
