class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while(itr):
            if(itr.data == data_after):
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

    def remove_by_value(self,data):
        if(self.head.data == data):
            self.head = self.head.next
            return
        
        itr = self.head
        while(itr.next):
            if(itr.next.data == data):
                itr.next = itr.next.next
                break
            itr = itr.next
        

    def print_list(self):
        node = self.head
        lstr = '['

        while(node):
            lstr += str(node.data)
            if(node.next):
                lstr += ","
            node = node.next
        
        lstr += ']'
        print(lstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    ll.insert_after_value(4,2)
    ll.remove_by_value(3)
    ll.print_list()