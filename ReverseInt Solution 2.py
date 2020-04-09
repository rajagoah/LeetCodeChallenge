def ReverseInt(x):
    #declaring a temporary holding variable (temp) and a variable to hold the reverse of the number (rev)
    temp = 0
    rev = 0
    #iterating through the digits in the varaible
    while x != 0:
        #pop operation (achieved by using mod operator and push operation achieved by the summation operation)
        temp = temp*10 + x%10
        x = x//10
        rev = temp
    return rev

if __name__=="__main__":
    print(ReverseInt(123))