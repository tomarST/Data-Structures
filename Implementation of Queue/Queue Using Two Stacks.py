class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass
class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()# remove last item from list
class Queue(object):
    def __init__(self):
        self.S1=ArrayStack()
        self.S2=ArrayStack()
    def is_Empty(self):
        return self.S1.is_empty()
    def size(self):
        self.S1.size
    def first(self):
        while not self.S1.is_empty():
            self.S2.push(self.S1.pop())
        temp=S2.pop()
        self.S1.push(self.S2.pop())
        while not self.S2.is_empty():
            self.S1.push(self.S2.pop())
        return temp
    def enqueue(self,k):
        self.S1.push(k)
    def dequeue(self):
        while not self.S1.is_empty():
            self.S2.push(self.S1.pop())
        temp=S2.pop()
        while not self.S2.is_empty():
            self.S1.push(self.S2.pop())
        return temp
        
        
    
