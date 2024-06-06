# 24264: 알고리즘 수업 - 알고리즘의 수행 시간 3

# 첫째 줄에 코드1 의 수행 횟수를 출력한다.
# 둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.
'''
def MenOfPassion(A, n):
    sum = 0
    for i in range(1, n):
        for j in range(1, n):
            sum = sum + A[i] * A[j]
    return sum
'''

# O(n2)의 시간 복잡도
n = int(input())

print(n**2)
print(2)
