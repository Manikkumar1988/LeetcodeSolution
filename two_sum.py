class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        firstIndex = 0
        lastIndex = 0
        for a in nums:
            #print('h: ', a,target-a)
            if target - a in nums:
                lastIndex = nums.index(target - a)
                #print('lastIndex: ', lastIndex)
                if lastIndex!= firstIndex:
                    break
            firstIndex = firstIndex + 1
        list = [firstIndex, lastIndex]
        return list


solution = Solution();
print(solution.twoSum([2, 7, 11, 15], 9))
