#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def twoSum(nums, target):
    #declaring a list to store the index values
    lst = []
    nums_small = []
    print("start here")

    #adding filter condition to reduce the size of the incoming list of records
    if len(str(target)) <= 2:
        for k in nums:
            if len(str(k)) <= len(str(target)) and k < target:
                nums_small.append(k)
            elif target == 0 and k == target:
                nums_small.append(k)
            else:
                continue
        print("#**********************#filtered input set#**********************s\n", nums_small)

        #iterator to parse through the values in the nums list
        for i in range(len(nums_small)):
            #**********************#**********************#**********************
            #Handling conditions where every element in the list occurs only once
            # **********************#**********************#**********************
            if nums_small.count(nums_small[i]) == 1:
                #creating a new list that will be iterated upon to get the addition of 2 numbers
                nums2 = nums_small[i+1:]
                #second iterator
                for j in range(len(nums2)):
                    #conditional operator to check if the sum of two numbers in the list is equal to target
                    if nums_small[i] + nums2[j] == target:
                        lst.append(nums_small.index(nums_small[i]))
                        lst.append(nums_small.index(nums2[j]))
                        return lst

            #**********************#**********************#**********************
            #Handling conditions where there are elements that occur more than once
            #**********************#**********************#**********************
            elif nums_small.count(nums_small[i]) > 1:
                # creating a new list that will be iterated upon to get the addition of 2 numbers
                nums2 = nums_small[i + 1:]

                #creating a list containing the Indices of repeating records
                indx = []

                #condition to decide which index is appended to the indx list
                for k in range(len(nums_small)):
                    if nums_small.count(nums[k]) > 1:
                      indx.append(k)

                # second iterator
                for j in range(len(nums2)):
                    # conditional operator to check if the sum of two numbers in the list is equal to target
                    if nums_small[i] + nums2[j] == target:
                        lst = indx
                        return lst
                    else:
                        continue

if __name__=="__main__":
    nums = [0,4,3,0]
    print(twoSum(nums, 0))

