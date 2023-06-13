
# QIes 1
t.c = O(n)
s.c = O(1)


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        count = 0
        a1 = a2 = head
        while a1:
            count += 1
            a1 = a1.next

        middleindex = count // 2
        for _ in range(middleindex - 1):
            a2 = a2.next
        a2.next = a2.next.next
        return head

# Ques2
t.c = o(n)
s.c = O(1)

def haslooop(self,head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True





# Ques 3
t.c = O(n)
s.c= O(n)

def nthnode(head,n,i):
    if head == None:
        return 1
    
    i += 1
    if i == n:
        print(head.data)
        return i
    
    return nthnode(head.next,n,i)



# Ques 4
t.c = O(n)
s.c = O(n)


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_linked_list(slow.next)
    
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev





# Ques 5
t.c = O(n)
s.c = O(n)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=' —> ')
        curr = curr.next
    print('None')
 
 
def removeCycle(head):
    prev = None        
    curr = head        
 
    s = set()
 
    while curr:
        if curr in s:
            prev.next = None
            return
 
        s.add(curr)
 
        prev = curr
        curr = curr.next



# Ques 6
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNode(head_ref, new_data):
    new_node = Node(new_data)
    new_node.next = head_ref
    head_ref = new_node

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, "-> ", end="")
        temp = temp.next
    print("Null")

def deleteNNodesAfterMNodes(head, M, N):
    if M == 0 or N == 0:
        return head

    current = head
    while current:
        # Skip M nodes
        for _ in range(M-1):
            if current is None:
                return head
            current = current.next

        if current is None:
            return head

        # Delete N nodes
        temp = current.next
        for _ in range(N):
            if temp is None:
                break
            next_node = temp.next
            temp = None
            temp = next_node
        
        current.next = temp
        current = current.next
    
    return head




# Ques 7
class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
  
class LinkedList(object):
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
          
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
              
    def merge(self, p, q):
        a_curr = p.head
        b_curr = q.head
  
        while a_curr != None and b_curr != None:
  
            a = a_curr.next
            b = b_curr.next
  
            b_curr.next = a
            a_curr.next = b_curr


            a_curr = a
            b_curr = b
            q.head = b_curr


# QUes 8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next

        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False  

