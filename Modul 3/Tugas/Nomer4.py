class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
 
    def print_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
 
    def print_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data)
            current = current.prev
 
    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
 
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
# membuat linked list baru
#dllist = DoublyLinkedList()
# menambahkan simpul baru
#dllist.add_to_end(4)
#dllist.add_to_end(5)
#dllist.add_to_beginning(3)
#dllist.add_to_beginning(2)
#dllist.add_to_beginning(1)

# mencetak isi linked list dari depan
#print("Linked List dari depan:")
#dllist.print_forward()

# mencetak isi linked list dari belakang
#print("Linked List dari belakang:")
#dllist.print_backward()
