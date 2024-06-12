# 10828: 스택

'''
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
push, pop, size, empty, top
'''

import sys 
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    s = input().split()     
    # ex) push 1: s[0] == 'push', s[1] == '1
    if s[0] == 'push':
        stack.append(s[1])
    elif s[0] == 'pop':
        if len(stack) > 0: 
            print(stack.pop())
        else: 
            print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if len(stack) == 0: 
            print(1)
        else: 
            print(0)
    elif s[0] == 'top':
        if len(stack) > 0: 
            print(stack[-1])
        else: 
            print(-1)