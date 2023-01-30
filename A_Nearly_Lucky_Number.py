from collections import Counter
digits = Counter(input())

luckyDigitNum = digits.get('4', 0) + digits.get('7', 0) 
print('YES') if luckyDigitNum == 4 or luckyDigitNum == 7 else print('NO')