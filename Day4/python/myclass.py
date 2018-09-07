#!/usr/bin/python

class Point():

 #this is a python constructor and it gets invoked automatically which an object of point is created

 #self represent current object(this)
 def __init__(self):
     print( 'Constructor got invoked ...')
     self.x = 0
     self.y = 0

 def setvalues(self, x, y):
     self.x = x
     self.y = y

 def printvalues(self):
     print( 'Value of x is ', self.x)
     print( 'Value of y is ', self.y)

def main():
    point1 = Point()
    point1.setvalues ( 10, 20 )
    point1.printvalues()

    point2 = Point()
    point2.setvalues ( 10, 40 )
    point2.printvalues()

main()
