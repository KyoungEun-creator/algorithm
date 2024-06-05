# 9506: 약수들의 합

# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)
# 입력의 마지막엔 -1이 주어진다.
# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.
# n이 완전수(어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같은 수)라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다.
# 이때, 약수들은 오름차순으로 나열해야 한다.
# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

while True:
    n = int(input())
    if n == -1:
        break 

    # 약수를 담는 리스트
    arr = []
    for i in range (1, n):
        if n % i == 0:
            arr.append(i)

    # n이 완전수일 때
    if sum(arr) == n:
        print(f"{n} =", end=" ")
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(arr[i])
            else:
                print(arr[i], "+", end=" ")

        # print(n, "=", end=" ")
        # print(*arr, sep=" + ")

    # n이 완전수가 아닐 때
    else:
        print(f"{n} is NOT perfect.")

