from itertools import product

if __name__ == "__main__":
    rawA = str(input())
    rawB = str(input())
    l1 = rawA.split()
    l2 = rawB.split()
    final = product(l1,l2)
    string = ''
    for x,y in final:
        string += '('+x+', '+y+') '

    print(string[:-1])