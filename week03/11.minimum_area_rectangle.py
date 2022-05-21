# TC: O(N^2)  Here N = len  of the points array
# MC: O(n)Here N = len  of the points array

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        points_set = set()
        

        min_area =  float("inf")
        
        for  point1 in points:
            for point2 in points_set:
                if point1[0] != point2[0] and point1[1] != point2[1]:
                    third_point = (point1[0], point2[1]) 
                    fourth_point = (point2[0], point1[1])
                
                    if third_point  in points_set and fourth_point in points_set:
                        area  = abs(point1[0] - point2[0]) * abs(point1[1]-point2[1])
                        min_area  = min(min_area, area)
                        
            points_set.add((point1[0], point1[1]))
                        
        if min_area == float("inf"):
            return 0
        
        return min_area