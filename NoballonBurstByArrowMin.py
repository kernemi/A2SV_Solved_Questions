class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key= lambda x:x[1] )
        arrows = 1
        arrpos = points[0][1]

        for start, end in points:
            if start > arrpos:
                arrows +=1
                arrpos = end
        return arrows

        
