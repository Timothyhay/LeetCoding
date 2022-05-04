'''
    Array
    Fix 1 value then do as 2Sum. 

    2sum:
    def twoSum(self, nums, target):
        buffer_dictionary = {}
        for i in rangenums.__len()):
            if nums[i] in buffer_dictionary:
                return [buffer_dictionary[nums[i]], i] #if a number shows up in the dictionary already that means the 
                                                        #necesarry pair has been iterated on previously
            else: # else is entirely optional
                buffer_dictionary[target - nums[i]] = i 
                # we insert the required number to pair with should it exist later in the list of numbers
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for fid in range(len(nums)-2):
            a = nums[fid]
            # Put diff dict here - clear for every fixed num
            diff = dict()
            for i in range(fid+1, len(nums)):
                if nums[i] in diff:
                    if [a, diff[nums[i]], nums[i]] not in ans:
                        ans.append([a, diff[nums[i]], nums[i]])
                else:
                    diff[-a-nums[i]] = nums[i]
        
        return ans