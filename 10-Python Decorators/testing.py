#!/usr/bin/env python


def printtest():
    print("Hello")



def printdecorator(intakefunc):
    def wrapperfunc():
        print("Before decoration")
        intakefunc()
        print("after the docoration")



##############----------

def div(a,b):
    return a/b
#print("Hello World")

div(3,5)
