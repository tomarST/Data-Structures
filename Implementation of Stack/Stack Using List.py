class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return bool(self.items==[])
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def main():
    s=Stack()
    print(s.isEmpty())
    s.push(1)
    print(s.size())
main()

def st(lst,k):
    for e in lst:
        if k-e in lst:
            return "True"
        else:
            return "False"
