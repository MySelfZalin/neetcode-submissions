class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()   #nums = [-1,-1,0,1,2,4,6]     
        for counter in range(0, len(nums) - 2):
            if counter > 0 and nums[counter] == nums[counter - 1]:
                continue

            i = nums[counter]
            if i > 0:
                return res

            need_sum = -i

            left = counter + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == need_sum:
                    res.append([i, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                
                elif curr_sum > need_sum:
                    right -= 1

                else:
                    left += 1
        
        return res                

                      
        
        