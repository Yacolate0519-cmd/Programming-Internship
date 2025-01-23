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

data = [i for i in range(1,11)]
result = list_to_linked_list(data)
print_linked_list(result)

def merge_two_linked_list(list1 , list2):
    head = ListNode(0)
    current = head
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return head.next

list1 = [1,2,4]
list2 = [1,3,4]
list1 = list_to_linked_list(list1)
list2 = list_to_linked_list(list2)

result1 = merge_two_linked_list(list1 , list2)
print_linked_list(result1)

