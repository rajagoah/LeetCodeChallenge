class Computer():
    def __init__(self):
        self.age = 21
        self.name = "Raj"

class nodes():
    def __init__(self, data):
        self.d = data
        self.next = None

class linked():
    def __init__(self):
        self.head = None

    def printing(self):
        data = self.head
        print("the data type of the incoming variable   : ", type(data))
        print("the value is                             : ", data.d)
        print("the address of value is                  : ", data)
        print("the address of value in second node is   : ", data.next)
        print("the value is                             : ", data.next.d)
        while data is not None:
            print(data.d)
            data = data.next

    def AtEnd(self, data):
        NewNode = nodes(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode



"""
#calling computer class
c1 = Computer()

print("id ", id(c1))
print("the memory address is        : ", c1)

#calling node class
n = nodes(1)
print("the details of the node are     : ", n)

#calling linked class
l = linked()
print("linked object are           : ", l)
print("linked class field          : ", l.head)
"""
#creating a main function where all the fields can be called within any class
if __name__=="__main__":
    combined_obj = linked()
    #print("the linked() object      : ", type(combined_obj))

    x = combined_obj.head = nodes(1)
    #print("data type of head var    : ", type(x))
    #print("nodes() object is        : ", x)

    x2 = nodes(2)

    #setting the address of the second element in the node to the first linked list
    x.next = x2
    #print("the address of x2 is     : ", x2)
    #print("the value of x2 is       : ", x2.d)

    #printing the linked list
    combined_obj.printing()

    #adding an element to the end
    linked.AtEnd("3")


