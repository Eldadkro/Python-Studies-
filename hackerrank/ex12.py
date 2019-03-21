from itertools import combinations

#calculates the probability to get 'a' from a given squence 
#input : int n(size), string , int k (amount of choises)
#prints the correct probability with at least 3 digits accurisy 
#idea = calc the combination of (n,k) then with Inclusion–exclusion principle clac the amount of a's( could look for the amount that a doesnt show and subtrackst from the total)
#takes way more time to think , and I have a PC to count for me 
#or ca

if __name__ == "__main__":
    N = int(input())
    string = str(input())
    listOfItems = string.split()
    k = int(input())
    args = []
    combinationss  = list(combinations(listOfItems,k))
    counter = 0
    for x in combinationss:
        if 'a' in x:
            counter += 1
    print(counter/len(combinationss))
    