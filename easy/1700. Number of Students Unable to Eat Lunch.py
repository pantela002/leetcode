from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = {1:0, 0:0}
        for i in students:
            if i==1:
                stud[1]+=1
            else:
                stud[0]+=1

        for i in sandwiches:
            if i==1:
                if stud[1]>0:
                    stud[1]-=1
                else:
                    return stud[0]+stud[1]
            else:
                if stud[0]>0:
                    stud[0]-=1
                else:
                    return stud[0]+stud[1]      

