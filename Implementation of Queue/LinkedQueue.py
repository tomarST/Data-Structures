class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue(object):
    def __init__(self):
        self.head=None
        self.next=None
        self.size=0
    def is_Empty(self):
        return self.head==None
    def size(self):
        return self.size
    def enqueue(self,k):
        if self.head==None:
            self.head=Node(k)
            self.size=1
        else:
            newNode=Node(k)
            newNode.next=self.head
            self.head=newNode
            self.size+=1
    def first(self):
        curNode=self.head
        while curNode.next!=None:
            curNode=curNode.next
        return curNode.value
    def dequeue(self):
        curNode=self.head
        prevNode=None
        while curNode.next!=None:
            prevNode=curNode
            curNode=curNode.next
        prevNode.next=None
        self.size-=1
        return curNode.value
Q=Queue()
print(Q.is_Empty())
Q.enqueue(5)
Q.enqueue(4)
Q.enqueue(3)
Q.enqueue(2)
Q.enqueue(1)
print(Q.dequeue())
print(Q.first())
print(Q.size)
