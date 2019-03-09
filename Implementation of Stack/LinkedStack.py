class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedStack(object):
    def __init__(self):
        self.head=None
        self.next=None
    def __len__(self):
        curNode=self.head
        count=0
        while curNode!=None:
            curNode=curNode.next
            count+=1
        return count
            
    def is_empty(self):
        return self.head==None
    def push(self,a):
        newElement=Node(a)
        newElement.next=self.head
        self.head=newElement
    def pop(self):
        temp=self.head
        self.head=self.head.next
        return temp.value
    def top(self):
        return self.head.value
s=LinkedStack()
print(s.is_empty())
s.push(5)
print(s.is_empty())
s.push(6)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
s.push(1)
print(s.top())
print(len(s))
