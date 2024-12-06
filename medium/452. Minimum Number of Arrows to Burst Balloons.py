from functools import cmp_to_key

class Solution:
    def comp(self, point1, point2):
        if point1[0] == point2[0]:
            return 1 if point1[1]>point2[1] else -1
        return  1 if point1[0]>point2[0] else -1
        
    def sort_array(self, points):
        return sorted(points, key=cmp_to_key(self.comp))

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points= self.sort_array(points)
        arrows = 0
        i=0
        while i<len(points):
            pom=i
            arrows+=1
            while pom<len(points) and points[pom][0] < points[i][1]:
                pom+=1
                arrows+=1
            pom=i
        return arrows
        