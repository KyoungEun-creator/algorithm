# title: 숫자의 개수

# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지.

# numbers = [int(input()) for _ in range(3)]
A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))   # ['1', '7', '0', '3', '7', '3', '0', '0']

# 방법1
for i in range (10):
    print(result.count(str(i))) # '1'이 몇 개, '2'가 몇 개, ...

# 방법2
count = [0] * 10                # [0,0,0,0,0,0,0,0,0,0] 초기화
for elem in result:
    count[int(elem)] += 1
for i in range(10):
    print(count[i])
    

