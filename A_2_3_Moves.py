'''
If the given input n is one the ansower will always be 2

If the given input n is divisible by 3 that is the minimum distance to reach there
How ever if it is not that means the number is less than by 2 or less than by 1 from any number that are divisible by 3

so if it's less than by 2 we can just add 1 to our answer since we can take 2 step
if it's less than by 1 we can also add 1 to our answer this is becaouse we will tak (n // 3) - 1 step and 3 + 1 = 4 wich is two 2 steps

that means if the number is not divisible by 3 we can just add 1
'''

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
        continue

    ans = n // 3 
    # if n is less by 1 or 2 from any number divisible by 3
    # if it's less by 1 we can take (n // 3) - 1 step and additional 2 * 2 step 
    # if it's less by two we can take (n // 3) step and 2 additonal step
    if n % 3:
        ans += 1

    print(ans)