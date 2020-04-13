class nodes():
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

if __name__ == "__main__":
    #assigning value to data element
    e1 = nodes("mon")
    e2 = nodes("tue")
    e3 = nodes("wed")

    #assigning value to pointer variable
    e1.nextval = e2
    e2.nextval = e3

