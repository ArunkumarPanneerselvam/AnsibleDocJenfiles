#!/usr/bin/python

def sayHello(msg): 
 print ( str( type(msg) ) + ' ==> ' + str( msg ) )

def main ():
    sayHello('Python')
    sayHello(10)

main()
