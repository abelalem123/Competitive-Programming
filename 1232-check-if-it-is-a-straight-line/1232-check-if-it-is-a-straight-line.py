class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Get the coordinates of the first two points
        point1 = coordinates[0]
        point2 = coordinates[1]
        
        # Calculate the slope between the first two points
        deltaX = point2[0] - point1[0]
        deltaY = point2[1] - point1[1]
        
        # Iterate through the remaining points
        for i in range(2, len(coordinates)):
            currentPoint = coordinates[i]
            
            # Calculate the slope between the current point and the first point
            currentDeltaX = currentPoint[0] - point1[0]
            currentDeltaY = currentPoint[1] - point1[1]
           
            if deltaX * currentDeltaY != deltaY * currentDeltaX:
                return False
        
        # All slopes are the same, so the points make a straight line
        return True