import sort

class linklist():
    class Node():
        def __init__(self,value):
            self.data = value
            self.next = None

    def __init__(self,value):
        self.head = self.Node(value)
        self.head.next = None

    def insert(self, value):
        new_node = self.Node(value)
        new_node.next = self.head.next
        self.head.next = new_node


    def delet(self,value):
        current = self.head.next
        previous = None

        while current is not None:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head.next
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

if __name__ == "__main__":
    List1 = linklist(1)
    a = [5,4,3,2,1]
    a = sort.bubble_sort(a)
    for value in a:
        List1.insert(value)

    List1.display()



