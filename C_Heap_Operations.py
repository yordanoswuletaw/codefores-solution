from heapq import heappush, heappop
def main():
    n = int(input())
    heap = []
    ops = []

    for _ in range(n):
        curr_op = input()
        if 'insert' in curr_op:
            op, num = curr_op.split()
            ops.append(op + ' ' + num)
            heappush(heap, int(num))
        elif 'getMin' in curr_op:
            op, num = curr_op.split()
            num = int(num)
            while heap and heap[0] < num:
                heappop(heap)
                ops.append('removeMin')
            if not heap or heap[0] > num:
                ops.append('insert ' + str(num)) 
                heappush(heap, num)
                ops.append(op + ' ' + str(num))
            elif heap[0] == num:
               ops.append(op + ' ' + str(num)) 
        else:
            if heap:
                heappop(heap)
                ops.append(curr_op) 
            else:
                ops.append('insert 0')
                ops.append(curr_op)

    print(len(ops))
    for op in ops:
        print(op)
    
if __name__ == '__main__':
    main()
 
 