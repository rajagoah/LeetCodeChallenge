#Given a 32-bit signed integer, reverse digits of an integer.

def RevInt(x):
    print(int(str(x)[::-1]))

if __name__ =="__main__":
    print(RevInt(350))