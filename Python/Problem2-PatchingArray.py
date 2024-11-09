class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        maxNumGen = 0
        lenNum = len(nums)
        output = 0
        i = 0
        while(maxNumGen < n):
            if i < lenNum:
                if maxNumGen + 1 >= nums[i]:
                    maxNumGen += nums[i]
                    i += 1
                else:
                    output += 1
                    maxNumGen += maxNumGen + 1   
            else:
                output += 1
                maxNumGen += maxNumGen + 1   
 
        return output