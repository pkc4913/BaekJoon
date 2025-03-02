import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 설정

# 첫 번째 줄: 건물 개수 입력
N = int(sys.stdin.readline().strip())

# 건물 정보 저장 (건설 시간, 선행 조건)
bt = [0] * N  # 건설 시간 저장 (0-based index)
dep = [[] for _ in range(N)]  # 선행 건물 목록
tbts = [-1] * N  # 최소 건설 시간 저장 (초기값 -1)

# N개의 줄 입력 처리
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    bt[i] = data[0]  # 첫 번째 값: 건설 시간
    for pre in data[1:-1]:  # 마지막 -1을 제외한 선행 건물 목록 저장
        dep[i].append(pre - 1)  # 1-based -> 0-based 변환

# 최소 건설 시간을 구하는 재귀 함수 (메모이제이션 적용)
def dp(bui):
    if tbts[bui] != -1:  # 이미 계산된 경우 반환
        return tbts[bui]

    if not dep[bui]:  # 선행 건물이 없는 경우
        tbts[bui] = bt[bui]
        return tbts[bui]

    max_pre_time = 0  # 선행 건물 중 가장 오래 걸리는 시간 찾기
    for pre in dep[bui]:
        max_pre_time = max(max_pre_time, dp(pre))

    tbts[bui] = bt[bui] + max_pre_time  # 현재 건물의 건설 시간 + 선행 건물 중 최대 시간
    return tbts[bui]

# 모든 건물에 대해 최소 건설 시간 계산
for i in range(N):
    dp(i)

# 결과 출력
for i in range(N):
    print(tbts[i])