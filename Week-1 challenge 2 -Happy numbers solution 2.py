#Write an algorithm to determine if a number is "happy".

#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits,
#and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
#a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers
import math
num = 19

#delcaring a list to store values coming out of sum operation
seen = []
if num == 1:
    print('True')
else:
    while num != 1:
        current = num
        sum = 0
        while current != 0:
            sum += (current%10) * (current%10)
            current = current // 10
            print("sum -- ", sum)
        num = sum

        if seen.__contains__(sum):
            print('false')
            break
        else:
            seen.append(sum)
        if sum == 1:
            print('true')





