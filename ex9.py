from itertools import combinations_with_replacement

#You are given a string . 
#Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

def printTuple(tup):
    for x in tup:
        print(x,end = '')



if __name__ == "__main__":
    raw = str(input())
    t = raw.partition(' ')
    string  = t[0]
    k = int(t[2])
    s = list(string)
    s.sort()
    for x in list(combinations_with_replacement(s,k)):
        printTuple(x)
        print('')
