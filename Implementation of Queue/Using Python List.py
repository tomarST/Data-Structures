class Queue(object):
    def __init__(self):
        self.L=[]
        self.size=0
    def is_Empty(self):
        return self.L==[]
    def size(self):
        return self.size
    def first(self):
        return self.L[0]
    def enqueue(self,k):
        self.append(k)
        self.size+=1
    def top(self):
        return self.L[0]
    def dequeue(self):
        g=self.L.pop(0)
        self.size-=1
        return g
        
    
