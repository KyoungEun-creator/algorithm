# title: 최댓값

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.


# 24/10/08
arr = []
for _ in range(9) :
    n = int(input())
    arr.append(n)

max_val = max(arr)
print(max_val)
print(arr.index(max_val)+1)

# old
arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)
# arr = [int(input()) for _ in range(9)]

max_val = max(arr)
print(max_val, arr.index(max_val)+1)

