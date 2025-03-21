import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
works = []
max_deadline = 0
for _ in range(N):
    d, w = map(int, input().split())  # 마감까지 남은 날짜 수, 점수
    max_deadline = max(max_deadline, d)
    heapq.heappush(works, (-d, w))

answer = 0
candidate_works = []
for day in range(max_deadline, 0, -1):
    # 할 수 있는 과제 == (day <= deadline)
    while works and day <= -works[0][0]:
        d_minus, w = heapq.heappop(works)
        heapq.heappush(candidate_works, (-w, -d_minus))
    if len(candidate_works) > 0:
        w_minus, d = heapq.heappop(candidate_works)
        answer += -w_minus
print(answer)
