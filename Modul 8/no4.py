class PriorityQueue():
    def __init__(self,item,priority):
        self.item = item
        self.priority= priority

class Priorityqueue():
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,item,priority):
        _PriorityQue(self.qlist,(item,priority))
        self.qlist.append(entry)
    def dequeue(self):
        n = []
        for i in self.qlist:
            n.append(i.priority)
        print (self.qlist.pop(n.index(min(n))).item)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]



   
a = PriorityQueue()
a.enqueue("rohmad", 5)
a.enqueue("khoir", 2)
a.enqueue("udin", 11)
a.enqueue("khoirudin", 6)
print("ProrityQueue Front==>",a.getFrontMost())
print("PriorityQueue Rear",a.getRearMost())