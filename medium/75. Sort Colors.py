class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        niz = [0,0,0]
        for i in nums:
            niz[i]+=1
        ind=0
        for i in range(len(niz)):
            for j in range(niz[i]):
                nums[ind]=i
                ind+=1
