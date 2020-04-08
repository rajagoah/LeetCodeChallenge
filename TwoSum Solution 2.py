#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

#importing pacakge
from collections import defaultdict as dd

def twoSum(nums, target):
    #declaring a list to store the index values
    lst = []
    lst_2 = []
    dic = {}
    print("start here")

    #first iterator to add the elements to the dictionary
    for i in range(len(nums)):
        #using a variable to store the current value of the iterator to be used to extract correct indices
        current = i

        dic.setdefault(nums[i],[]).append(nums.index(nums[i],current))
        #dic[nums[i]] = nums.index(nums[i],current)

    print("dictionary is: ", dic)
        #iterator for parsing the input list
    for j in range(len(nums)):
        if dic.keys().__contains__(target - nums[j]):
            lst.append(dic.get(target - nums[j]))
    for k in lst:
        print(k)
        lst_2.append(k[0])
    print('list 2 is: ',lst_2)

    #sorting the list in ascending order
    lst_2.sort()
    lst.sort()
    return lst_2

if __name__=="__main__":
    nums = [2,7,11,15]
    print(twoSum(nums,9))