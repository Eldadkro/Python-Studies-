from itertools import combinations

#You are given a string . 
#Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

def printTuple(tup):
    for x in tup:
        print(x,end = '')



if __name__ == "__main__":
    raw = str(input())
    t = raw.partition(' ')
    string  = t[0]
    k = int(t[2])
    for i in range(1,k+1):
        s = list(string)
        s.sort()
        for x in list(combinations(s,i)):
            printTuple(x)
            print('')
