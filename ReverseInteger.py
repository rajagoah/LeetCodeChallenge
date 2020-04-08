#Given a 32-bit signed integer, reverse digits of an integer.

def RevInt(x):
    if x > 0:
        return int(str(x)[::-1])
    elif x < 0:
        return -1*int(str(abs(x))[::-1])
    elif x == 0:
        return 0

if __name__ =="__main__":
    print(RevInt(0))