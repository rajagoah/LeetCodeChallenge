#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
nums = [1,2,3,3,4]

dic = {}

for i in nums:
    dic.setdefault(i,0)
    dic[i] = dic[i] + 1

for k,v in dic.items():
    if v == 1:
        print(k)