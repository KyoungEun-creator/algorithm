# 2587: 대표값2

'''
첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 주어지는 자연수는 100 보다 작은 10의 배수이다.
첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 자연수이다.
'''

# 방법1
'''
arr = []
for _ in range(5):
    num = int(input())
    arr.append(num)

# 중앙값을 찾기 위한 오름차순 정렬
arr.sort()

avg_val = sum(arr) // 5
center_val = arr[2]

print(avg_val)
print(center_val)
'''

# 방법2
arr = [int(input()) for i in range(5)]
print(sum(arr) // 5)
print(sorted(arr)[2])


