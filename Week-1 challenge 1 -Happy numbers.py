#Write an algorithm to determine if a number is "happy".

#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits,
#and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
#a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers

num = 11

#coverting to string to iterate through it
num_Str = str(num)

#declaring variables
happy_num = 0
lst_num = []

#iterating through the string
while len(str(num_Str)) != 1:
    for i in range(len(num_Str)):
        lst_num.append(int(num_Str[i]))

    for i in lst_num:
        happy_num = (i*i) + happy_num
        print(happy_num)
        num_Str = str(happy_num)


