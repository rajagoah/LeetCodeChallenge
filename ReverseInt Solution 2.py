def ReverseInt(x):
    #declaring a temporary holding variable (temp) and a variable to hold the reverse of the number (rev)
    current = x
    temp = 0
    rev = 0
    if current >= 0 and len(str(current))< 10:
        #iterating through the digits in the varaible
        while current != 0:
            #pop operation (achieved by using mod operator and push operation achieved by the summation operation)
            temp = temp*10 + current%10
            current = current//10
            rev = temp
        return rev
    elif current < 0 and len(str(current))< 10:
        current = abs(current)
        while current != 0:
           # pop operation (achieved by using mod operator and push operation achieved by the summation operation)
           temp = temp * 10 + current % 10
           current = current // 10
           rev = temp
        return rev*-1
    elif len(str(current)) >= 10:
        return 0

if __name__=="__main__":
    print(ReverseInt(12345678987654321))