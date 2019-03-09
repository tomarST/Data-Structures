class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
def small(head):
    small=head
    curNode=head.next
    small_prev=None
    small_next=None
    prevNode=head
    while curNode!=None:
        if curNode.data<small.data:
            small=curNode
            small_prev=prevNode
            small_next=curNode.next
        prevNode=curNode
        curNode=curNode.next
    small_prev.next=small_next
    small.next=head
    head=small
    return head
head=Node(5)
b=Node(2)
c=Node(3)
d=Node(1)
head.next=b
b.next=c
c.next=d
curN=small(head)
while curN!=None:
    print(curN.data)
    curN=curN.next
