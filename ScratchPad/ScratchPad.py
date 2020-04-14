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

#calling computer class
c1 = Computer()

print("id ", id(c1))
print("the memory address is: ", c1)

#calling node class
n = nodes(1)
print("the details of the node are: ", n)

#calling linked class
l = linked()
print("the details of the linked object are: ", l)
print("calling the field in the linked class: ", l.head)

#creating a main function where all the fields can be called within any class
if __name__=="__main__":
    combined_obj = linked()
    print("the combined object has been created to be of Linked() class ", type(combined_obj))

    x = combined_obj.head = nodes(1)
    print("the combined object's head field has been instantiated with the nodes class ", type(x))
    print("the memory of the combined_obj.head variable of nodes() class is, ", x)



