##Rectangle class definition
##Author: 
##Date: 12/3/2024

from geometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, p1,p2):
        GeometricObject.__init__(self)
        self.p1 = p1
        self.p2 = p2
        
    def _draw(self,aturtle):
        #Add code here
        
