# 11653: 소인수분해

# 정수 N이 주어졌을 때, 
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

N = int(input())

# 소인수를 담은 리스트
arr = []

i = 2
while N != 1:
    if N % i == 0:
        arr.append(i)
        N = N // i
    else:
        i += 1

# 오름차순 정렬
arr.sort()

# 한 줄에 하나씩 출력
for elem in arr:
    print(elem)