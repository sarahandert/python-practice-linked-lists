"""Name: Sarah Andert
    Course: CMPS 1500
    Lab Section: Tuesday, CMPS 1501-05 11-12.15 pm
    Assignment: lab9pr0ab.py
    Date: 11/29/2018
    A function that takes as input the front nodes of two linked lists, and links those two linked lists together.
    L1: a->b->c->none
    L2: d->e->f->none
    >>>>>>
    a->b->c->d->e->f->none

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

L = Node(a)         # the data node
L.next = Node(b)        # the next node
L.next.next = Node(c)

L2 = Node(d)         # the data node
L2.next = Node(e)        # the next node
L2.next.next = Node(f)

def join(head1, head2):
    current = head1
    while current.next!= None:
        current = current.next
    current.next = head2
    return head1


    
""" The symptotic runtime of the function would be linear time, O(n), because in order to append the second linked list
to the first one, you need to traverse the whole first linked list to find the tail node first
"""
