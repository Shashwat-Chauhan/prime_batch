class ListNode:
    def __init__(self, val = 0 , next=None):
        self.val = val
        self.next = None

n1 = ListNode(10)
head = n1


# <--------------------  Add Node to the end of the List  ------------------>
def addNode(head, val):
    new_node = ListNode(val)

    if head is None:
        return new_node
    
    temp = head
    while(temp.next):
        temp = temp.next
    
    temp.next = new_node
    
    return head



def printList(head):
    temp = head
    while(temp):
        print(temp.val , end=" -> ")
        temp = temp.next
    print("None")
    return 

printList(head)

# <-------------------- Delete k'th node from the linked list ------------------>

def deleteKthNode(head, k):
    if head is None or k <= 0:
        return head
    
    if k == 1:
        if head.next is None:
            head = None
            return head
        temp = head
        head = head.next
        del(temp)   
        return head

    temp = head
    cnt = 1
    while(temp.next):
        if cnt == k-1:
            to_delete = temp.next
            temp.next = temp.next.next
            del(to_delete)
            break
        temp = temp.next
        cnt += 1
    return head

# <------------------ Insert Node at the Kth position of the linked list --------------->
def insertAtK(head, k, val):
    if k == 1:
        new_node = ListNode(val)
        new_node.next = head
        head = new_node
        return head

    cnt = 1
    temp = head
    while(temp.next):
        if cnt == k-1:
            new_node = ListNode(val)
            new_node.next = temp.next
            temp.next = new_node
            break
        temp = temp.next
        cnt += 1

    return head
    


        


addNode(head, 20)
addNode(head, 30)
addNode(head, 40)
addNode(head, 50)

# head = deleteKthNode(head , 3)
# head = deleteKthNode(head , 2)
# head = deleteKthNode(head , 2)
# head = deleteKthNode(head , 2)
# head = deleteKthNode(head , 1)

printList(head)

insertAtK(head , 2 , 69)

printList(head)