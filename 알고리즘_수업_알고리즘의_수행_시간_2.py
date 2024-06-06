# 24263: 알고리즘 수업 - 알고리즘의 수행 시간 2

# 아래 알고리즘의 수행 횟수 출력
# 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력
'''
def MenOfPassion(A, n):
    sum = 0
    for i in range(1, n):
        sum += A[i]
    return sum
'''

# O(n)의 시간 복잡도
n = int(input())

print(n)
print(1)

