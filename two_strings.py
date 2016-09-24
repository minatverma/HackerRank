#!/bin/python

def two_strings():
    n = int(raw_input())
    name_list = []
    for i in xrange(n):
        name_list.append(raw_input())
    print name_list
    return True


if __name__ == '__main__':
    two_strings()
