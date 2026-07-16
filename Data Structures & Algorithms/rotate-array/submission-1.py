class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_array(arr: List[int], left: int, right: int) -> List[int]:
            while left < right:
                arr[left], arr[right] = arr[right], nums[left]
                left += 1
                right -= 1
            return arr    

        rev_modul = k % len(nums)
        if rev_modul == 0:
            return

        reverse_array(nums, 0, len(nums)-1)
        
        reverse_array(nums, 0, rev_modul - 1)
        reverse_array(nums, rev_modul, len(nums)-1)