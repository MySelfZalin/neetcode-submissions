class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        hight = len(matrix) - 1

        while low <= hight:
            mid = (low+hight) // 2
            subb_min, subb_max = matrix[mid][0], matrix[mid][-1]

            if subb_min <= target and subb_max >= target:
                return self.binary_search(matrix[mid], target)

            #[1,2,3,4,5,6,7]
            elif target < subb_min:
                hight = mid - 1

            else:
                low = mid + 1
        return False        

    def binary_search(self, nums, target):
        low = 0
        hight = len(nums) - 1

        while low <= hight:
            mid = (low+hight) // 2 
            guess = nums[mid]


            if guess == target:
                return True

            elif guess < target:
                low = mid + 1

            else:
                hight = mid - 1
        return False



        