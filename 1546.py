# title: 평균

# 시험 본 과목의 개수 N (N <= 1000)
N = int(input())
# 세준이의 현재 성적
scores = list(map(int, input().split()))

max_score = max(scores)

for i in range(N):
    scores[i] = scores[i] / max_score * 100
    
print(sum(scores)/N)


