import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())  # 보석 개수, 가방 개수

jewels = []
for _ in range(N):
    m, v = map(int, input().split())  # 무게, 가격
    heapq.heappush(jewels, (m, v))

bags = []
for _ in range(K):
    c = int(input().strip())  # 담을 수 있는 최대 무게
    bags.append(c)
bags.sort()

answer = 0
candidate_prices = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        m, v = heapq.heappop(jewels)
        heapq.heappush(candidate_prices, -v)
    if len(candidate_prices) > 0:
        max_price = -heapq.heappop(candidate_prices)
        answer += max_price
print(answer)
