borzeCode = input()
decoded = ''
i = 0
while i < len(borzeCode):
    if borzeCode[i] == '.':
        decoded += '0'
    else:
        if borzeCode[i + 1] == '.':
            decoded += '1'
        else:
            decoded += '2'
        i += 1
    i += 1
print(decoded)
