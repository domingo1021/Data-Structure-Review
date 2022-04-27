class ListNode():
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def search(self, key):
        # While loop, O(n)
        # If not found, return the last node's node.next, which is None
        node = self
        while node != None:
            if node.data == key:
                return node
            node = node.next
        return node

    def search_recursive(self, key):
        # Recursive的作法, O(n)
        node = self
        if node.data == key:
            return node
        else: return node.next.search_recursive(key)

    def insert(self, new_node):
        # 對某個Node進行新增, O(1)
        new_node.next = self.next
        self.next = new_node

    def delete_next_node(self):
        # O(1)
        self.next = self.next.next

    def delete_current_node(self):
        # O(1)
        self.data = self.next.data

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __str__(self):
        #print all information of the node and the remaining all nodes.
        node = self
        message = ""
        while node.data:
            message += str(node.data)
            if node.next is not None:
                message+="->"
                node = node.next
            else: return message

if __name__ == "__main__":
    x = [1,2,3,4,5]
    seperate = "-"*10 + "\n"

    # Initialize linked list object
    # Print out all information about
    print("all information")
    head = None
    for element in x:
        if head is None:
            head = ListNode(element)
            tail = head
        else:
            tail.next = ListNode(element)
            tail = tail.next
    print(head)
    print(seperate)

    # Make ListNode iterable
    print("Iteration: ")
    for node in head:
        print(node.data)
    print(seperate)

    #delete node
    print("Deleting next")
    head.delete_next_node()
    print(head)
    print(seperate)

    #insert
    print("Inserting..")
    head.insert(ListNode(100))
    print(head)
    print(seperate)

    #Search
    print("Searching..")
    print(head.search(3))
    print(head.search(100000))
    print(seperate)
