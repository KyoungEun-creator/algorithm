# 1992: 쿼드트리

'''
입력
첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.

출력
영상을 압축한 결과를 출력한다.
'''

import sys
N = int(input())
video = [list(input().strip()) for _ in range(N)]

def quadTree(x, y, size):
    check = video[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != check:
                mid = size // 2
                return "(" + quadTree(x, y, mid) + quadTree(x, y + mid, mid) + quadTree(x + mid, y, mid) + quadTree(x + mid, y + mid, mid) + ")"
            
    return check
 
print(quadTree(0, 0, N))