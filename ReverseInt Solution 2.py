def ReverseInt(x):
    #declaring a temporary holding variable (temp) and a variable to hold the reverse of the number (rev)
    current = abs(x)
    temp = 0
    rev = 0

    if current >= 0:
        #iterating through the digits in the varaible
        while current != 0:
            #pop operation (achieved by using mod operator and push operation achieved by the summation operation)
            temp = temp*10 + current%10
            current = current//10
            rev = temp
        return rev
    if current < 0:
       while current != 0:
           # pop operation (achieved by using mod operator and push operation achieved by the summation operation)
           temp = temp * 10 + current % 10
           current = current // 10
           rev = temp
       return rev*-1

if __name__=="__main__":
    print(ReverseInt(-656))