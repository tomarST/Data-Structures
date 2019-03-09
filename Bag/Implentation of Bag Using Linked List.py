
class Node(object):
    def __init__(self,value):
        self.data=value
        self.next=None
class Bag(object):
    def __init__(self):
        self.head=None
        self.size=0
    def size(self):
        return self.size
    def is_empty(self):
        return self.head==None
    def add(self,item):
        newItem=Node(item)
        newItem.next=self.head
        self.head=newItem
        self.size+=1
    def contains(self,a):
        curNode=self.head
        count=0
        while curNode.next!=None:
            if curNode.data == a:
                count+=1
            curNode=curNode.next
        return bool(count>0)
    def occur(self,a):
        curNode=self.head
        count=0
        while curNode!=None:
            if curNode.data == a:
                count+=1
            curNode=curNode.next
        return count
    def remove(self,a):
        prevNode=None
        curNode=self.head
        if curNode.data == a:
            self.head=self.head.next
        else:
            while curNode.data!=a:
                prevNode=curNode
                curNode=curNode.next
            prevNode.next=curNode.next
        self.size=self.size-1
    def remove_all(self,a):
        c=self.occur(a)
        for i in range(c):
            self.remove(a)
                
    def printContents(self):
        curNode=self.head
        while curNode!=None:
            print(curNode.data)
            curNode=curNode.next
b=Bag()
#Adding elements to an emty bag
print(b.is_empty())
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(1)
b.add(2)
b.remove_all(2)#Removing all the entries of 2 in bag
b.printContents()#Printing the contents of bag
print(b.occur(5))#Checking How many times an element occured
print(b.contains(8))#Checking if bag has this element or not
print("No.of items in bag:",b.size)

