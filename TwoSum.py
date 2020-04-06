#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def twoSum(nums, target):
    #declaring a list to store the index values
    lst = []
    #iterator to parse through the values in the nums list
    for i in range(len(nums)):

        #**********************#**********************#**********************
        #Handling conditions where every element in the list occurs only once
        # **********************#**********************#**********************
        if nums.count(nums[i]) == 1:
            #creating a new list that will be iterated upon to get the addition of 2 numbers
            nums2 = nums[i+1:]
            #second iterator
            for j in range(len(nums2)):
                #conditional operator to check if the sum of two numbers in the list is equal to target
                if nums[i] + nums2[j] == target:
                    print(nums2)
                    lst.append(nums.index(nums[i]))
                    lst.append(nums.index(nums2[j]))
                    return lst

        #**********************#**********************#**********************
        #Handling conditions where there are elements that occur more than once
        #**********************#**********************#**********************
        elif nums.count(nums[i]) > 1:
            # creating a new list that will be iterated upon to get the addition of 2 numbers
            nums2 = nums[i + 1:]

            # second iterator
            for j in range(len(nums2)):

                # conditional operator to check if the sum of two numbers in the list is equal to target
                if nums[i] + nums2[j] == target:
                    print(nums2)
                    # edge case 1 handling --> when there are repeating values in the list
                    if nums[i] == nums2[j] and len(nums2) >= 1:
                        lst.append(nums.index(nums[i]))
                        lst.append(nums2.index(nums2[j]))
                        lst[1] += 1
                    return lst
                else:
                    continue

if __name__=="__main__":
    nums = [2,5,5,11]
    print(twoSum(nums, 10))