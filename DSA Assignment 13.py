
# Ques 1
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
def insert(start, item):
 
    temp = Node(0)
    temp.data = item
    temp.next = None
 
    if (start == None):
        start = temp
    else :
        a = start
        while (a.next != None):
            a = a.next
 
        a.next = temp
         
    return start
 
def newList(start1, start2):
 
    a1 = start1
    a2 = start2
     
    start = None
    while (a1 != None) :
        temp = Node(0)
        temp.next = None
 
        if (a1.data < a2.data):
            temp.data = a2.data
        else:
            temp.data = a1.data
 
        if (start == None):
            start = temp
        else :
            a = start
            while (a.next != None):
                a = a.next
 
            a.next = temp
         
        a1 = a1.next
        a2 = a2.next
     
    return start
 
def display(start):
 
    while (start != None) :
        print(start.data, "->", end = " ")
        start = start.next
     
    print(" ")

# Ques 2
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr:
            while curr.next and curr.next.val==curr.val:
                curr.next=curr.next.next
            curr=curr.next
        return head
    

# Ques 3
def reverseInGroups(head, k):
    if head is None:
        return None

    current = head
    prev = None
    next = None
    count = 0

    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    if next is not None:
        head.next = reverseInGroups(next, k)

    return prev

# Ques 4
class Node:
  
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
  
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        if next is not None:
            head.next = self.reverse(next, k)
  
        return prev
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next


# Ques 5
class Node:
    def __init__(self, new_data):
        
        self.data = new_data
        self.next = None
def deleteLast(head, x):
    temp = head
    ptr = None
    
    while (temp != None):
        if (temp.data == x):
            ptr = temp    
        temp = temp.next
    
    if (ptr != None and ptr.next == None):
        temp = head
        while (temp.next != ptr):
            temp = temp.next
            
        temp.next = None
    
    if (ptr != None and ptr.next != None):
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next
        
    return head
    
def newNode(x):
    node = Node(0)
    node.data = x
    node.next = None
    return node
def display(head):
    temp = head
    if (head == None):
        print("NULL\n")
        return
    
    while (temp != None):
        print( temp.data, end = " ")
        temp = temp.next
    
    print("NULL")



# Ques 6
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
         
 
def newNode(key):
    return Node(key)


# Ques 7
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


def reverse_list(head):
    temp_node = None
    current_node = head

    while current_node is not None:
        
        temp_node = current_node.prev
        current_node.prev = current_node.next
        current_node.next = temp_node

        current_node = current_node.prev

    if temp_node is not None:
        head = temp_node.prev

    return head


# Ques 8
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


def delete_node(head, del_node):
    if head is None or del_node is None:
        return

    if head == del_node:
        head = del_node.next

    if del_node.next is not None:
        del_node.next.prev = del_node.prev

    if del_node.prev is not None:
        del_node.prev.next = del_node.next

    del_node.next = None
    del_node.prev = None


def deleteNodeAtPositionN(head, N):
    if head is None or N <= 0:
        return

    current = head
    for i in range(1, N):
        if current is None:
            return
        current = current.next

    if current is None:
        return

    delete_node(head, current)


def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head

    if head is not None:
        head.prev = new_node

    head = new_node


def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
