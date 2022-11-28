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

    def insert_at_end(self, data):
        node = Node(data, None)
        itr = self.head
        if itr is None:
            self.head = node
            return

        while(itr.next):
            itr = itr.next
        itr.next = node
    def insert_values(self, list_data):
        self.head = None
        for data in list_data:
            self.insert_at_end(data)
    
    def length_of_linkedlist(self):
        if self.head == None:
            print(0)
            return

        else:
            i = 0
            while(self.head!=None):
                self.head = self.head.next
                i+=1
            print(i)

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
    # llst.insert_at_beg(22)
    # llst.insert_at_beg(32)
    # llst.insert_at_end(12)
    # new_ll = [1,2,3,4,5,5,6,8]
    # llst.insert_values(new_ll)
    llst.printer()
    llst.length_of_linkedlist()
