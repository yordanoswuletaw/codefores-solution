def solve():
    src = input().lower()
    dest = input().lower()
    srcPt, destPt = None, None

    for i in range(8, 0, -1):
        for j, char in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            if char + str(i) == src:
                srcPt = (8 - i, j)
            if char + str(i) == dest:
                destPt = ( 8 - i, j)

    
    def dfs(srcPt, destPt, moves):
        srcX, srcY = srcPt
        destX, destY = destPt

        if srcX == destX and srcY == destY:
            return moves
        elif srcX > destX and srcY > destY:
            moves.append('LU')
            return dfs((srcX - 1, srcY - 1), destPt, moves)
        elif srcX < destX and srcY < destY:
            moves.append('RD')
            return dfs((srcX + 1, srcY + 1), destPt, moves)
        elif srcX < destX and srcY > destY:
            moves.append('LD')
            return dfs((srcX + 1, srcY - 1), destPt, moves)
        elif srcX > destX and srcY < destY:
            moves.append('RU')
            return dfs((srcX - 1, srcY + 1), destPt, moves)
        elif srcX < destX and srcY == destY:
            moves.append('D')
            return dfs((srcX + 1, srcY), destPt, moves)
        elif srcX > destX and srcY == destY:
            moves.append('U')
            return dfs((srcX - 1, srcY), destPt, moves)
        elif srcX == destX and srcY < destY:
            moves.append('R')
            return dfs((srcX, srcY + 1), destPt, moves)
        elif srcX == destX and srcY > destY:
            moves.append('L')
            return dfs((srcX, srcY - 1), destPt, moves)
    
    moves = dfs(srcPt, destPt, [])
    print(len(moves))
    for move in moves:
        print(move)

solve()