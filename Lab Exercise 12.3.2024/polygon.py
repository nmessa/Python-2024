##Polygon class definition
##Author: 
##Date: 12/3/2024

from geometricObject import GeometricObject

class Polygon(GeometricObject):
    def __init__(self, p1, sides,length):
        GeometricObject.__init__(self)
        self.start = p1
        self.sideLength = length
        self.numsides = sides
        
    def _draw(self,aturtle):
        #Add code here
        
