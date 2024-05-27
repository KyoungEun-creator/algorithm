# title: 직각삼각형

# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하기
# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
# 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[1] == 0 and arr[1] == 0:
        break
    arr.sort()  # 오름차순 정렬

    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print("right")
    else:
        print("wrong")
        