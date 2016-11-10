#!/bin/env python

def main():
    PM = eval(input("What is today's PM2.5?"))
    print PM
    if PM > 75:
        print("Unhealthy. Be careful!")
    if PM < 35:
        print ("Good. GO running!")
main()
