# 2839: 설탕 배달

'''
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
상근이가 배달하는 봉지의 최소 개수를 출력한다. 
만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''

# 방법1
'''
N = int(input())

# N kg을 만들기 위해 필요한 봉지 개수(3킬로그램 봉지와 5킬로그램 봉지 개수 합)의 리스트
sum_arr = []

for i in range(0, N // 5 + 1):
    for j in range(0, N // 3 + 1):
        if 5 * i + 3 * j == N:
            sum_arr.append(i + j)
            break

if sum_arr:
    print(min(sum_arr))
else:
    print(-1)
'''

# 방법2
'''
sugar = int(input())

bags = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bags += sugar // 5
        print(bags)
        break
    # 5의 배수가 될 때까지 설탕 - 3, 봉지 + 1
    sugar -= 3      
    bags += 1
else:
    print(-1)
'''

# 방법3 - 시간복잡도 good
n = int(input())
cnt = 0
 
while True:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break   
    elif n % 5 != 0:
        n -= 3
        cnt += 1

    # 남은 무게가 음수가 된 경우 (남은 무게가 0이면 깔끔하게 나눠떨어졌음 을 의미)
    if n < 0:
        print(-1)   # 정확하게 무게를 맞출 수 없음을 의미
        break       # 루프 종료
