from itertools import groupby

#You are given a string . Suppose a character '' occurs consecutively  
#times in the string. Replace these consecutive occurrences 
# of the character 'c' with (x,c) in the string.

def groupToString(group):
    string = ''
    for item in group:
        string += str(item)
    return string

if __name__ == "__main__":
    s = str(input())
    final = ''
    for k,g in groupby(s):
        tmp = groupToString(g)
        final += '('+str(len(tmp))+', '+str(k)+') '
    print(final[:-1])

