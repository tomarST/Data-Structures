class LinkedList(object):
    def __init__(self,a):
        self.data=a
        self.next=None
l=LinkedList(5)
k=LinkedList(10)
g=LinkedList(15)
l.next=k
k.next=g
print(g.next.data)
