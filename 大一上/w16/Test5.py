# class ListNode:
#     def __init__(self , value , next = None):
#         self.value = value
#         self.next = next
    
# def list_to_linked_list(data):
#     if not data:
#         return None;
#     head = ListNode(data[0])
#     current = head
#     for value in data[1:]:
#         current.next = ListNode(value)
#         current = current.next
#     return head

# def print_linked_list(head):
#     if not head:
#         return None
#     elements = []
#     while head:
#         elements.append(str(head.value))
#         head = head.next
#     print(' -> '.join(elements))

# def odd_even_linked_list(head):
#     if not head or not head.next:
#         return None
#     odd = ListNode(0)
#     even = ListNode(0)
#     odd_tail , even_tail = odd , even
    
#     current = head
#     while current:
#         if current.value % 2 == 1:
#             odd_tail.next = current
#             odd_tail = odd_tail.next
#         elif current.value % 2 == 0:
#             even_tail.next = current
#             even_tail = even_tail.next
#         current = current.next
#     even_tail.next = None
#     odd_tail.next = even.next
#     return odd.next

# def merge_two_ListNode(list1 , list2):
#     head = ListNode(0)
#     current = head
#     while list1 and list2:
#         if list1.value < list2.value:
#             current.next = list1
#             list1 =  list1.next
#         else:
#             current.next = list2
#             list2 = list2.next
#         current = current.next
#     if not list1:
#         current.next = list2
#     elif not list2:
#         current.next = list1
#     return head.next
# data = [1,2,3,4,5,6,7,8,9,10]

# list1 = [1,2,4]
# list2 = [1,3,4]

# list1 = list_to_linked_list(list1)
# list2 = list_to_linked_list(list2)

# result1 = merge_two_ListNode(list1,list2)

# result = list_to_linked_list(data)

# result = odd_even_linked_list(result)

# print_linked_list(result)
# print('--'*30)
# print_linked_list(result1)

class ListNode:
    def __init__(self , value , next = None):
        self.value = value
        self.next = next

def list_to_linked_list(data):
    if not data:
        return None
    head = ListNode(data[0])
    current = head
    for value in data[1:]:
        current.next = ListNode(value)
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
    
def odd_even_linked_list(head):
    if not head:
        return None
    odd = ListNode(0)
    even = ListNode(0)
    odd_tail , even_tail = odd , even
    
    current = head
    while current:
        if current.value % 2 == 1:
            odd_tail.next = current
            odd_tail = odd_tail.next
        elif current.value % 2 == 0:
            even_tail.next = current
            even_tail = even_tail.next
        current = current.next
    odd_tail.next = odd.next
    even_tail.next = None   
    return odd.next

data = [i for i in range(1,11)]

result = list_to_linked_list(data)

print_linked_list(result)

print('--'*30)

result = odd_even_linked_list(result)
print_linked_list(result)
