#Given a non empty linked list with head node 'Head', return the middle node. if there are two middle node, then return the second mid node
#we need to create a linked list
#creating a node class
class Node:

    #Function to initialize the Node object
    def __int__(self, data):
        self.data = data #Assign the data
        self.next = None #Assign the next value to null

#creating a linkedlist class:
class LinkedList(self):

    #Function to initialize the head of the linked list
    def __init__(self):
        self.head = None


#def ListNode(x):
#    leng = len(x)
#    #condition to deal with lists with even length
#    if leng%2 != 0:
#        mid_len = int(leng/2)
#        print(x[mid_len])
#    elif leng%2 == 0:
#        mid_len = int(leng/2)
#        print(x[mid_len])

if __name__=="__main__":

    #start with an empty list
    Llist = LinkedList()

    Llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    Llist.head.next = second
    second.next = third