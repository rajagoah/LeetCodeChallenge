#Write an algorithm to determine if a number is "happy".

#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits,
#and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
#a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers
import math
num = 19

# declaring variables
happy_num = 0
last_dig = 0

while num != 0:
    last_dig = num % 10
    num = math.floor(num // 10)
    # using the mod operator to store the last digit of an integer
    happy_num = (last_dig * last_dig) + happy_num
    num = happy_num





