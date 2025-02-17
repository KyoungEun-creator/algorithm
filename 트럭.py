# 133335: 트럭

'''
입력
입력 데이터는 표준입력을 사용한다. 입력은 두 줄로 이루어진다. 
입력의 첫 번째 줄에는 세 개의 정수 n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)이 주어지는데, n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다. 
입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데, 
ai는 i번째 트럭의 무게를 나타낸다.

출력
출력은 표준출력을 사용한다. 모든 트럭들이 다리를 건너는 최단시간을 출력하라.
'''

from collections import deque

n, w, L = list(map(int, input().split()))
trucks = deque(map(int, input().split()))

# 다리 길이
bridge = deque([0] * w)
# 다리 위 총 무게
bridge_weight = 0
# 소요 시간
time = 0

# trucks가 아직 남아있고, bridge가 텅비기 전까지
while trucks or sum(bridge) > 0:
    time += 1
    # bridge를 빠져나가는 트럭의 무게 빼줌
    bridge_weight -= bridge.popleft()

    if trucks and bridge_weight + trucks[0] <= L:
        new_truck = trucks.popleft() # 트럭에서 빼서
        bridge.append(new_truck) # 다리에 넣어줌
        bridge_weight += new_truck # 다리 무게 추가됨
    else:
        bridge.append(0)

print(time)


