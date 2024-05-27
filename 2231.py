# title: 분해합

# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구하라.
# 256의 생성자는 245
# 생성자가 없는 경우에는 0을 출력

n = int(input())    # 입력받은 분해합: 256
res = 0             # 생성자

nums = list(map(int, str(n))) # [2, 5, 6]

for i in range(n+1):
    temp = i + sum(map(int, str(i)))    # i + (i의 각 자리의 수의 합)
    if (temp == n):                     # 현재 값과 입력받은 분해합이 서로 같다면
        res = i         
        break                           # 가장 작은 값 찾아냈을 때 멈춰버리기 위함

print(res)                               # if문에 해당하지 않는 조건이라면 처음에 설정했던 res 값 0이 된다          