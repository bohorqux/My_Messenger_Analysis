#!/usr/bin/python3

from threadfunctions import *
from construct_data import *
from stringformatting import *

def main():
    threads = initThreads("messages.htm")
    print("Testing lead_zeros() function...")

    test1 = ""
    test2 = "1"
    test3 = "10"
    test4 = "100"
    test5 = "1000"

    zeros = 4

    print("\n************")
    print("Test Case: 1")
    print("String = %s\tNum Zeros = %d" % (test1,zeros))
    print("\nexpected: %s\nresult: %s\n" % ("0000", lead_zeros(test1, zeros)))
    print("***********")

    print("\n************")
    print("Test Case: 2")
    print("String = %s\tNum Zeros = %d" % (test2,zeros))
    print("\nexpected: %s\nresult: %s\n" % ("0001", lead_zeros(test2, zeros)))
    print("***********")

    print("\n************")
    print("Test Case: 3")
    print("String = %s\tNum Zeros = %d" % (test3,zeros))
    print("\nexpected: %s\nresult: %s\n" % ("0010", lead_zeros(test3, zeros)))
    print("***********")

    print("\n************")
    print("Test Case: 4")
    print("String = %s\tNum Zeros = %d" % (test4,zeros))
    print("\nexpected: %s\nresult: %s\n" % ("0100", lead_zeros(test4, zeros)))
    print("***********")

    print("\n************")
    print("Test Case: 5")
    print("String = %s\tNum Zeros = %d" % (test5,zeros))
    print("\nexpected: %s\nresult: %s\n" % ("1000", lead_zeros(test5, zeros)))
    print("***********")

main()
