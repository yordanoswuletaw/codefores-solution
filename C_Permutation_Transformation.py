import sys, threading

input = lambda: sys.stdin.readline().strip()


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def __init__(self):
        self.result = [] 
    
    def transform(self, perms):
        if len(perms) <= 0:
            return None 
        maxIndx = perms.index(max(perms))
        root = TreeNode(perms[maxIndx])
        root.left = self.transform(perms[:maxIndx])
        root.right = self.transform(perms[maxIndx + 1:])

        return root
    
    def preOrder(self, root, level):
        if not root:
            return 
        self.preOrder(root.left, level + 1)
        self.result.append(level)
        self.preOrder(root.right, level + 1)


def main():
    for _ in range(int(input())):
        n = int(input())
        perms = list(map(int, input().split()))
        solution = Solution()
        solution.preOrder(solution.transform(perms), 0)
        print(*solution.result)


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

