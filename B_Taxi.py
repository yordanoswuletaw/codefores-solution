from collections import Counter
from math import ceil
def main():
    n = int(input())

    # grouping groups
    hashMap = Counter( map(int, input().split()))

    # assigning car for groups with 4 memembers
    cars = hashMap[4] 

    # assigning car for groups with 3 memebers
    cars += hashMap[3]
    hashMap[1] -= hashMap[3]

    # assinging car for groups with 2 members
    cars += hashMap[2] // 2
    rem = hashMap[2] % 2
    cars += rem
    hashMap[1] -= 2 * rem
    
    # assigning car for groups with 1 memebrs
    if hashMap[1] > 0:
        cars += ceil(hashMap[1]/4)
    
    print(cars)
        

if __name__ == '__main__':
    main()

