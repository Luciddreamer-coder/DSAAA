

#Normal solution with O(n^2) time complexity
'''def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
'''
#Using Hash Map with O(n) time complexity
def twoSum(nums , target):
    number_map ={}   #empty hash map to store numbers and their indices
    for i , num in enumerate(nums):
        complement = target - num  #calculate the complement
        if complement in number_map:  #check if the complement exists in the hash map
            return [number_map[complement], i]  #return the indices of the complement and current number
        number_map[num] = i  #store the current number and its index in the hash map

#Using class 
class Solution:
    def twosum(self, nums, target):
        numer_map={}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in numer_map:
                return [numer_map[complement], i]
            numer_map[num] = i
    
test = Solution()
test.twosum([2, 7, 11, 15], 9)
print(test.twosum([2, 7, 11, 15], 9))

#print(twoSum([2, 7, 11, 15], 9))
#print(twoSum([3, 2, 4], 6))
#print(twoSum([3, 3], 6))

#Optimized solution with O(n) time complexity using a hash map