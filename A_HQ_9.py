def solution(inp):
    instructions = set('HQ9')
    for char in inp:
        if char in instructions:
            return 'YES'
    return 'NO'

def main():
    inp = input()
    print(solution(inp))


if __name__ == '__main__':
    main()