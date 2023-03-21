





    















n, l, r = map(int, input().split())

res = 0
count = 0
def compute(n):
    global res
    global count
    if count >= r:
        return
    if n == 0 or n == 1:
        if count >= l - 1 and count < r:
             res += n 
        count += 1
        return 
    compute(n // 2)  
    compute(n % 2)
    compute(n // 2)
        

compute(n)

print(res)

