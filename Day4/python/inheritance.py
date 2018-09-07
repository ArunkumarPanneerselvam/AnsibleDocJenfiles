#!/usr/bin/python

class Iphone6s: 

    def __init__(self):
        print( 'Iphone6s contructor invoked ...')

    def printSpec(self):
        print('Vendor : ' + 'Apple')
        print('Model : ' + 'IPhone')
        print('Front cam : ' + 'Yes')

class Iphone7(Iphone6s):

    def __init__(self):
        print ('Iphone6s contructor invoked ...')

    def printSpec(self):
        print('Rear cam : ' + 'Yes')
        Iphone6s.printSpec() 

def main():
    iphone7 = Iphone7()
    iphone7.printSpec()

main()
