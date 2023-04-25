def main():
    seq = sorted(map(int, input().split(',')))
    stdSeq, n = [], len(seq)

    left = right = seq[0]
    for i in range(1, n):
        if seq[i] - right > 1:
            if right - left >= 1:
                stdSeq.append(str(left) + '-' + str(right))
            else:
                stdSeq.append(str(right))
            left = right = seq[i]
        else:
            right = seq[i]

    if right - left >= 1:
        stdSeq.append(str(left) + '-' + str(right))
    else:
        stdSeq.append(str(right))

    
    print(','.join(stdSeq))


if __name__ == '__main__':
    main()

