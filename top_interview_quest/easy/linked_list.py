class Node:
    def __init__(self, data=None, next=None)->None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def printer(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)


if __name__=='__main__':
    llst = LinkedList()
    llst.insert_at_beg(22)
    llst.insert_at_beg(32)
    llst.printer()
