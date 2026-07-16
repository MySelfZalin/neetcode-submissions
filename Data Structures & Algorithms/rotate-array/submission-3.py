class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_array(left: int, right: int) -> List[int]:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1   

        rev_modul = k % len(nums)
        if rev_modul == 0:
            return

        reverse_array(0, len(nums)-1)
        
        reverse_array(0, rev_modul - 1)
        reverse_array(rev_modul, len(nums)-1)