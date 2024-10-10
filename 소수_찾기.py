# 1978: 소수 찾기

'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

N = int(input())
n = list(map(int, input().split()))  # [1,3,5,7]
res = 0 # 소수 개수
for elem in n:
    if elem > 1:
        cnt = 0 # 하나의 elem에 대한 약수 개수
        for i in range(2, elem):
            if elem % i == 0:
                cnt += 1
        if cnt == 0:
            res += 1
print(res)