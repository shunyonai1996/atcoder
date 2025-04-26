import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = list(map(int, input().split()))
a = set(int(input()) for _ in range(M))  # Convert to set for faster lookup
# pattern = 0

# print(N, M, a)

# # DFSでパターンを洗い出してDPで回答を管理
# # aのケースを削る



# # ans = pattern % 1000000007

# current: 今の段
# path: ここまでの経路

def dfs(current, path, N):
    # print(f"→ dfs({current}, {path})")

    if current == N:
        print(f"○ゴール到達: {path}")
        return

    if current > N:
        # print(f"●超過: {path} → return")
        return

    dfs(current + 1, path + [current + 1], N)
    dfs(current + 2, path + [current + 2], N)

dfs(0, [0], N)


print('===============')

def dfs(current, N):
    if current == N:
        return 1
    if current > N:
        return 0

    count1 = dfs(current + 1, N)
    count2 = dfs(current + 2, N)

    return count1 + count2

total_paths = dfs(0, N)
print(f"➡ 通り数: {total_paths}")

print('====================')

def dp_way(N):
    dp = [0] * (N + 2)
    dp[0] = 1

    for i in range(N):
        print(f'{i+1}回目のループ')
        print(f'dpの状態: {dp}')
        if i + 1 not in a:  # Skip broken steps
            dp[i + 1] += dp[i]
        if i + 2 not in a:  # Skip broken steps
            dp[i + 2] += dp[i]

        print(f"dp[{i+1}] = {dp[i+1]}, dp[{i+2}] = {dp[i+2]}")  # 状態表示

    return dp[N]

print(f"➡ 通り数 (DP): {dp_way(N)}")




# DP = Dynamic Programming（動的計画法）
# 「過去の結果を使い回して、計算を効率化するテクニック」
# 再計算を避けて、配列に答えを貯めていく
# 「問題を小さく分けて、その答えを使って大きな問題を解く」考え方
# よく出てくるキーワード：最小値、最大値、通り数、最短経路

# DFS = Depth-First Search（深さ優先探索）
# 「分岐のある道を、奥まで潜ってから戻って探索する方法」
# 木やグラフを探索するときによく使う
# 再帰やスタックで実装される
# 「まず1つの道を限界まで進み、そこが終わったら別の道を試す」タイプの探索