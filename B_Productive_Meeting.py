from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

def main():
    for _ in range(int(input())):
        n = int(input())
        sociability = list(map(int, input().split()))
        hashMap = {i: num for i, num in enumerate(sociability)}
        heap = [-1 * num for num in sociability]
        heapify(heap)

        person1 = person2 = None
        talks = 0
        output = []

        while heap:
            if not person1:
                minVal = -1 * heappop(heap)
                person1 = [hashMap[minVal], minVal]
            if not person2:
                minVal = -1 * heappop(heap)
                person2 = [hashMap[minVal], minVal]
            if person1 and person2:
                if person1[1] > person2[1]:
                    talks += person2[1]
                    output.append((person1[0], person2[0], person2[1]))
                    person1[1] -= person2[1]
                    person2 = None
                elif person1[1] < person2[1]:
                    talks += person1[1]
                    output.append((person1[0], person2[0], person1[1])) 
                    person2[1] -= person1[1]
                    person1=None
                else:
                    talks += person2[1]
                    output.append((person1[0], person2[0], person2[1]))
                    person1 = person2 = None
        print(talks)
        for i, j, k in output:
            for _ in range(k):
                print(i, j)


if __name__ == '__main__':
    main()