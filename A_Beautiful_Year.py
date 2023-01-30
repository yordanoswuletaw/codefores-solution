currYear = input()
nextYear = str(int(currYear) + 1)

while len(nextYear) != len(set(nextYear)):
    nextYear = str(int(nextYear) + 1)
print(nextYear)

       