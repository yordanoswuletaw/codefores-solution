def main():
    n = int(input())
    routine = list(map(int, input().split()))

    exercises = [0, 0, 0]
    for turn in range(n):
        exercises[turn % 3] += routine[turn]
    
    if exercises[0] > exercises[1] and exercises[0] > exercises[2]:
        print('chest')
    elif exercises[1] > exercises[2]:
        print('biceps')
    else:
        print('back')
    
if __name__ == '__main__':
    main()
