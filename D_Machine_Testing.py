from math import ceil
def main():
    for _ in range(int(input())):
        n = int(input())
        health = list(map(int, input().split())) 
        power = list(map(int, input().split())) 

        print('----------------')

        if n == 1:
            print(0)
        else:
            stack = []
            for i in range(len(attempt)):
                if stack and stack[-1][0] < attempt[i]:
                    currTime = currPower = 0
                    while stack and stack[-1][0] < attempt[i]:
                        currTime, currPower = stack.pop()
                        health[i + 1] -= currTime * power[i]
                        attempt[i] = (health)
                    remTime = ceil(health[i + 1] / currPower)
                    stack.append([currTime + remTime, currPower])
                else:
                    stack.append([attempt[i], power[i]])
                print(stack)
            
            print(stack[0][0])


if __name__ == '__main__':
    main()