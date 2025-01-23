class ListNode:
    def __init__(self , value , next = None):
        self.value = value
        self.next = next

def list_to_linked_list(data):
    if not data:
        return
    head = ListNode(0)
    current = head
    for value in data:
        current.next = ListNode(value)
        current = current.next
    return head.next

def print_linked_list(head):
    if not head:
        return 
    current = head
    count = 1
    while current:
        print(current.value , end = ' -> ')
        if count % 10 == 0:
            print()
        current = current.next
        count += 1
    print()

data = [x for x in range(1,51)]
data = list_to_linked_list(data)

print_linked_list(data)

def merge_two_sorted_list(list1 , list2):
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
    
def odd_even_linked_list(head):
    odd = ListNode(0)
    even = ListNode(0)
    odd_tail , even_tail = odd , even
    
    current = head 
    while current:
        if current.value % 2 == 1:
            odd_tail.next = current
            odd_tail = odd_tail.next
        else:
            even_tail.next = current
            even_tail = even_tail.next
        current = current.next
    odd_tail.next = odd.next
    even_tail.next = None
    return odd.next 
list1 = [1,2,4]
list2 = [1,3,4]
list1 = list_to_linked_list(list1)
list2 = list_to_linked_list(list2)
result = merge_two_sorted_list(list1 , list2)
print_linked_list(result)

data = [1,2,3,4,5,6,7,8,9,10]
data = list_to_linked_list(data)
data = odd_even_linked_list(data)
print_linked_list(data)