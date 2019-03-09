class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass
class ArrayQueue(object):
    def __init__(self):
        self.Q=[]
    def is_empty(self):
        return self.Q==[]
    def enqueue(self,a):
        self.Q.append(a)
    def dequeue(self):
        return self.Q.pop(0)
    def first(self):
        return self.Q[0]
    
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
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()# remove last item from list
def pald(S,Q):
    def transfer(S,Q):
        if S.is_empty():   #Base Case for Recursion 
            return 
        else:
            temp=S.pop()   #Saving top element of the Stack at each call
            Q.enqueue(temp) #Enqueing every top element of stack to queue at each call
            transfer(S,Q)   
            if temp==Q.first(): #Checking if the first element of queue(i.e top element of Original Stack) is same as Stack first element or not 
                S.push(temp)#if it is then we push the element to stack
                Q.dequeue()# AND dequeue the same element from Queue
    transfer(S,Q)#Calling the inner method
    return Q.is_empty() # if it's a palindrome then the queue will be empty if it's not then the string is not palindrome
S=ArrayStack()
Q=ArrayQueue()
S.push("r")
S.push("o")
S.push("t")
S.push("o")
S.push("e")
print(pald(S,Q))
