class PriorityQueue():
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data, priority):
        entry = PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def getFrontMost(self):
        x = 0
        while self.qlist[x].priority != 0:
            x+=1
        return self.qlist[x].item
    def getRearMost(self):
        thelist = []
        for i in self.qlist:
            thelist.append(i.priority)
        print (self.qlist[thelist.index(max(thelist))].item)

class PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

a = PriorityQueue()
a.enqueue("Jeruk", 4)
a.enqueue("Tomat", 2)
a.enqueue("Mangga", 0)
a.enqueue("Duku", 5)
a.enqueue("Pepaya", 2)

#print(a.getFrontMost())
#print(a.getRearMost())
