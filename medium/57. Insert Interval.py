class Solution:
    def insert(self, intervals, newInterval):
      if not intervals:
         return [newInterval]
      out_intervals= []
      if newInterval[1]<intervals[0][0]:
         out_intervals.append(newInterval)
         for i in intervals:
            out_intervals.append(i)
      elif newInterval[0]>intervals[-1][1]:
         for i in intervals:
            out_intervals.append(i)
         out_intervals.append(newInterval)
      else:
         start_ind=-1
         for i in range(len(intervals)):
            start_ind=i
            if newInterval[0]<=intervals[i][1]:  
               break

         end_ind = len(intervals)
         for i in range(len(intervals)-1,-1,-1):
            end_ind=i
            if newInterval[1]>=intervals[i][0]:  
               break
               
         for i in range(0,start_ind):
            out_intervals.append(intervals[i])
         out_intervals.append([min(newInterval[0],intervals[start_ind][0]),max(newInterval[1],intervals[end_ind][1])])
         for i in range(end_ind+1,len(intervals)):
            out_intervals.append(intervals[i])

      return out_intervals
      


intervals1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval1 = [4,8]
case1 = [intervals1,newInterval1]
intervals2 = [[1,3],[6,9]]
newInterval2 = [2,5]
case2=[intervals2,newInterval2]
task = Solution()
print(task.insert(case1[0],case1[1])) #Output: [[1,2],[3,10],[12,16]]

