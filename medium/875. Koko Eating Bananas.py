class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #   Input: piles = [3,6,7,11], h = 8
        #   Output: 4

        l = 0
        d = max(piles)
        m=len(piles)
        while l <= d:
            mid = l + (d - l)//2
            s=0
            for i in range(len(piles)):
                s+= piles[i]//mid if piles[i]%mid==0 else piles[i]//mid + 1
            if s<=h:
                if mid < m:
                    m=mid
                d = mid - 1
            else:
                l = mid + 1

        return m

                





        