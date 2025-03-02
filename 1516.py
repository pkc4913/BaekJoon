# 첫 번째 줄: 건물의 개수 입력
N = int(input().strip())

# 건물 정보 저장 (건설 시간, 선행 조건)
bt = [0] * (N+1)  # 건설 시간 저장 (1-based index)
dep = [[] for _ in range(N+1)]  # 선행 건물 목록

# N개의 줄 입력 처리
for i in range(1, N+1):
    data = list(map(int, input().split()))
    bt[i] = data[0]  # 첫 번째 값: 건설 시간
    dep[i] = data[1:-1]  # 마지막 -1을 제외한 선행 건물 목록 저장

tbt = [0] * (N+1)

def dp(bui):
    mbt = 0
    pres = list(dep[bui])
    if pres:  # 선행 건물이 있는 경우
        mbt = max(tbt[pre] for pre in pres)

# # 확인 출력
print("건물 개수:", N)
print("건설 시간:", bt[1:])
print("선행 조건:", dep[1:])