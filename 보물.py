# 1026: 보물
'''
길이가 N인 정수 배열 A와 B가 있다. 
S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 
단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 
셋째 줄에는 B에 있는 수가 순서대로 주어진다. 
N은 50보다 작거나 같은 자연수이고, 
A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.
'''

N = int(input())
A = list(map(int, input().split())) # 1 1 1 6 0
B = list(map(int, input().split())) # 2 7 8 3 1

sortedA = sorted(A)
sortedB = sorted(B, reverse=True)

S = 0
for i in range(N):
    S += sortedA[i] * sortedB[i]

print(S)