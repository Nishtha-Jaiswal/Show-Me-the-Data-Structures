
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
                   

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next   
        return out_string

    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
  
 
    def removal(self, rem_node):#removing duplicates
        node=self.head
        while node and node.next != rem_node:#fetching node previous to the node to be deleted
            node=node.next
        prev_node = node
        if prev_node is None:# node to be removed is the starting node
            self.head = self.head.next
        else:#making new links and removing the node
            prev_node.next = rem_node.next

def duplicates(llist):#finding dublicates
    node1 = llist.head
    while node1:
        node2=node1.next
        value=node1.value
        while node2:#each value is checked with every other value in the linked list
            temp=node2
            node2=node2.next
            if temp.value == value:#values are same
                llist.removal(temp)
        node1 = node1.next          


def union(llist_1, llist_2):
    union_result=LinkedList()
    head1=Node(None)
    head2=Node(None)
    head1=llist_1.head
    head2=llist_2.head
    while head1 is not None:
        union_result.append(head1.value)#linked list 1 appended
        head1=head1.next
    while head2 is not None:
        union_result.append(head2.value)#linked list 2 apended
        head2=head2.next
    duplicates(union_result)
    return union_result    

def intersection(llist_1,llist_2):
    intersection_result=LinkedList()
    head1=Node(None)
    head2=Node(None)
    head1=llist_1.head
    
    while head1:
        head2=llist_2.head
        temp=head1.value
        while head2:#every entry of the 2nd linked list is checked with a single value of 1st linked list
            if head2.value == temp:
                intersection_result.append(head2.value)
                break
            head2=head2.next#head2 goes to next node
        head1=head1.next#after first value of linked list 1 being checked with each value of linked list 2, now head 1 moves to next value and so on
    duplicates(intersection_result)
    return intersection_result
        


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
result = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))#3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
result = intersection(linked_list_1,linked_list_2)#4 -> 6 -> 21 ->
if result.head is None:
    print("no intersection")
else:
    print(result)             
                   

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
result= LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]


for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))#3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
result = intersection(linked_list_3,linked_list_4)#no intersection
if result.head is None:
    print("no intersection")
else:
    print(result)


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
result= LinkedList()

element_1 = [3,3,3,3,6,6,6,4,4,4]
element_2 = [3,3,6,6,4,4]


for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))#3 -> 6 -> 4 ->
result = intersection(linked_list_5,linked_list_6)#3 -> 6 -> 4 ->
if result.head is None:
    print("no intersection")
else:
    print(result)

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
result = LinkedList()
element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

res = union(linked_list_7,linked_list_8)#no union, both the lists are empty
if res.head is None:
    print("no union, both the lists are empty")
else:
    print(res)
result = intersection(linked_list_7,linked_list_8)#no intersection
if result.head is None:
    print("no intersection")
else:
    print(result)
