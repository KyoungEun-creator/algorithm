# 25305: 커트라인

'''
첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어진다.
둘째 줄에는 각 학생의 점수 x가 공백을 사이에 두고 주어진다.
커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.
상을 받는 커트라인을 출력하라.
'''

N, k = map(int, input().split())
scores = list(map(int, input().split()))

print(sorted(scores)[-k])

# scores.sort(reverse = True)
# print(scores[k-1])



