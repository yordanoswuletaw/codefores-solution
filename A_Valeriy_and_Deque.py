from collections import deque

def main():
    n, q = map(int, input().split()) 
    nums = deque(map(int, input().split()))
    maxIndx = nums.index(max(nums))
    
    before = []
    for i in range(maxIndx):
        num1, num2 = nums.popleft(), nums.popleft()
        before.append((num1, num2)) 
        if num1 > num2:
            nums.appendleft(num1)
            nums.append(num2)
        else:
            nums.appendleft(num2)
            nums.append(num1)

    after = []
    for i in range(n - 1):
      num1, num2 = nums.popleft(), nums.popleft()
      after.append((num1, num2))
      if num1 > num2:
          nums.appendleft(num1)
          nums.append(num2)
      else:
          nums.appendleft(num2)
          nums.append(num1)
    
    for _ in range(q):
        indx = int(input()) - 1
        if indx < maxIndx:
            print(*before[indx])
        else:
            indx -= maxIndx
            indx %= len(after)
            print(*after[indx])
            
if __name__ == '__main__':
    main()