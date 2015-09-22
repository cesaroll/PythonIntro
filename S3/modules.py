#Import Files
import tempconv

temp = 212
convTemp = tempconv.ftoc(temp)
print(str(temp) + " F equals is " + str(convTemp) + " C")

temp = 0
convTemp = tempconv.ctof(temp)
print(str(temp) + " C equals is " + str(convTemp) + " F")

#Import Shapes specific notation
#import shapes
from shapes import Shape
from shapes import Rectangle

s1 = Shape(4,8)
print(s1)

r1 = Rectangle(5, 10, 6, 8)
print(r1)
