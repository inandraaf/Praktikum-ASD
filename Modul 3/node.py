class Node(object):
    """Sebuah simpul di linked list"""
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def kunjungi(head):
     curNode = head
     while curNode is not None:
         print(curNode.data)
         curNode = curNode.next

# class DNode(object):
#     def __init__(self,data,next,prev):
#         self.data = data
#         self.next = next
#         self.prev = prev
    
