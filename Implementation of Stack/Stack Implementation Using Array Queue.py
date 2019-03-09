class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass
class ArrayQueue(object):
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self.data))     # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def _resize(self, cap):                  # we assume cap >= len(self)
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]            # intentionally shift indices
            walk = (1 + walk) % len(old)         # use old size as modulus
        self._front = 0                        # front has been realigned
class Stack(object):
    def __init__(self):
        self.q=ArrayQueue()
    def is_empty(self):
        return self.q.is_empty()
        
    def push(self,a):
        self.q.enqueue(a)
    def top(self):
        if self.q.is_empty():
            raise Empty('Stack is empty')
        l=len(self.q)
        for i in range(l):
            if i==l-1:
                temp1=self.q.dequeue()
                self.q.enqueue(temp1)
            else:
                temp=self.q.dequeue()
                self.q.enqueue(temp)
        return temp1
    def pop(self):
        if self.q.is_empty():
            raise Empty('Stack is empty')
        l=len(self.q)
        for i in range(l):
            if i==l-1:
                temp1=self.q.dequeue()
            else:
                temp=self.q.dequeue()
                self.q.enqueue(temp)
        return temp1
S=Stack()
S.push(5)
S.push(4)
S.push(3)
S.push(2)
print(S.pop())
print(S.pop())
