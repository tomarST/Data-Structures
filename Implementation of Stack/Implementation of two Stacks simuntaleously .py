class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass
class ArrayStack:
    n=200 #size of the combined stacks
    def __init__(self):
        self._data = [None]*ArrayStack.n
        self.even_index=0
        self.odd_index=ArrayStack.n
    def __len__(self):
        return len(self._data)
    def size1(self):
        return self.even_index
    def size2(self):
        return ArrayStack.n-self.odd_index

    def is_empty1(self):
        return self._data[:self.even_index+1]==[None]
    def is_empty2(self):
        return self._data[self.odd_index:]==[]
    def push(self, e):
      if self.even_index!=self.odd_index:
        if e%2 ==0:
          self._data[self.even_index]=e
          self.even_index+=1
        else:
          self.odd_index-=1
          self._data[self.odd_index]=e

    def top1(self):
        if self.is_empty1():
            raise Empty('Stack is empty')
        return self._data[self.even_index-1]
    def top2(self):
        if self.is_empty2():
            raise Empty('Stack is empty')
        return self._data[self.odd_index]
    def pop1(self):
        if self.is_empty1():
            raise Empty('Stack is empty')
        self.temp=self._data[self.even_index-1]
        self._data[self.even_index-1]=None
        self.even_index-=1
        return self.temp
    def pop2(self):
        if self.is_empty2():
            raise Empty('Stack is empty')
        self.temp=self._data[self.odd_index]
        self._data[self.odd_index]=None
        self.odd_index+=1
        return self.temp
if __name__ == '__main__':
    S = ArrayStack()
    print(S.is_empty1())
    print(S.is_empty2())
    for i in range(200):
      S.push(i)
    print(S.size1())
    print(S.size2())
    print(S.pop1())
    print(S.pop2())
    print(S.top1())
    print(S.top2())
