class ListNode:
    def __init__(self , value , next = None):
        self.value = value
        self.next = next

def list_to_linked_list(data):
    if not data:
        return None
    head = ListNode(data[0])
    current = head
    for i in data[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

def print_linked_list(head):
    if not head:
        return None
    elements = []
    while head:
        elements.append(str(head.value))
        head = head.next
    print(' -> '.join(elements))
    
data = [3,2,0,-1]
result = list_to_linked_list(data)

def check(head):
    if not head:
        return False
    slow , fast = head , head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = fast.next
        fast = fast.next.next
    return False


print_linked_list(result)

print(check(result))