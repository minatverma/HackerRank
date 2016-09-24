#!/bin/python

def get_inputs():
    n = int(raw_input())
    name_list = []
    for i in xrange(n*2):
        name_list.append(raw_input())
    return n, name_list


def get_substrings(string):
    for start_index in xrange(len(string)):
        for end_index in xrange(len(string) - start_index):
            # print start_index, end_index+1
            yield string[start_index:start_index+end_index+1]


def two_strings(src_string, tgt_string):
    result = 'NO'
    for sub in get_substrings(src_string):
        if sub in tgt_string:
            result = 'YES'
            break
    return result


if __name__ == '__main__':
    n, name_list = get_inputs()
    for i in xrange(0, n*2, 2):
        src_string = name_list[i]
        tgt_string = name_list[i + 1]
        print two_strings(src_string, tgt_string)
