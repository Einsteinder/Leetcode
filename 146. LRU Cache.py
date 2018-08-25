from collections import deque


class LRUCache:
    def __init__(self, capacity):
        self.max = capacity
        self.dic = {}
        self.q = deque()
        """
        :type capacity: int
        """

    def get(self, key):

        if key in self.dic:
            index = self.q.index(key)
            del self.q[index]
            self.q.append(key)
            return self.dic[key]
        else:
            return -1
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        if key in self.dic:
            index = self.q.index(key)
            del self.q[index]
            self.q.append(key)
            self.dic[key] = value


        else:
            if len(self.dic) > self.max - 1:
                lrukey = self.q.popleft()
                del self.dic[lrukey]

            self.dic[key] = value
            self.q.append(key)

        """
        :type key: int
        :type value: int
        :rtype: void
        """

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)