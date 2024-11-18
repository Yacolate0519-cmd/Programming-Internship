class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = next

map = {}
n_node = ListNode(None)
head1 = n_node

while head1 is not None:
    str = head1.val
    if str in map:
        head1 = head1.next
    else:
        map[str] = 1
        node = ListNode(str)
        n_node.next = node
        n_node = n_node.next
        head = head1.next
        