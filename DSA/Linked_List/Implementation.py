# Define a Node
class Node:
    def __init__(self, data):
        self.data = data    # Store data
        self.next = None    # Store reference to next node

# Define the Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:   # Traverse to the last node
            temp = temp.next
        temp.next = new_node

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node with specific value
    def delete_node(self, key):
        temp = self.head

        # If the head node holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Key not found.")
            return

        prev.next = temp.next
        temp = None

    # Search for a value
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("NULL")


ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_at_end(30)

ll.display()  # Output: 5 → 10 → 20 → 30 → NULL

ll.delete_node(20)
ll.display()  # Output: 5 → 10 → 30 → NULL

print("Search 10:", ll.search(10))  # Output: True
print("Search 100:", ll.search(100))  # Output: False

