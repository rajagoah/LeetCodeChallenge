#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def twoSum(nums, target):
    #declaring a list to store the index values
    lst = []
    dic = {}
    print("start here")

    #first iterator to add the elements to the dictionary
    for i in range(len(nums)):
        dic[nums[i]] = nums.index(nums[i])

    #iterator for parsing the input list
    for j in range(len(nums)):
        nums2 = nums[i+1:]
        if dic.__contains__(target - nums[i]):
            print(dic)
            break


if __name__=="__main__":
    nums = [3,2,3]
    print(twoSum(nums,6))