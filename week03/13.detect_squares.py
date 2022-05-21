# TC: O(N)  Here N = len  of the all points
# MC: O(N)

class DetectSquares:

    def __init__(self):
        self.visited_points = {}
        
    
    def add(self, point: List[int]) -> None:
        
        if (point[0], point[1]) in self.visited_points:
            self.visited_points[(point[0], point[1])] +=1
            
        else:
            self.visited_points[(point[0], point[1])]  = 1
        
    def count(self, point: List[int]) -> int:
        total = 0   
        for  visited_point in self.visited_points:
            third_point = (point[0], visited_point[1])
            fourth_point = (visited_point[0], point[1])
            
            if  point[1] != visited_point[1]  and abs(point[1] - visited_point[1]) == abs(point[0] - visited_point[0]):
                if third_point in self.visited_points and fourth_point in self.visited_points:
                    total += self.visited_points[third_point] *  self.visited_points[fourth_point] *  self.visited_points[visited_point]          
        
        return total
                    
