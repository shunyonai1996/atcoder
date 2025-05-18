N, M, Q = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(Q)]
A = [0] * N
ans = 0

def dfs(i):
    global ans
    if i == N:
        print(f"完成: {A}")
        score = 0
        for a_i, b_i, c_i, d_i in conditions:
            if A[b_i - 1] - A[a_i - 1] == c_i:
                score += d_i
        if score > ans:
            ans = score
        return

    start = A[i-1] if i > 0 else 1
    for v in range(start, M + 1):
        A[i] = v
        print(f"呼び出し前: i={i}, v={v}, A={A}")
        dfs(i + 1)
        print(f"戻ってきた: i={i}, v={v}, A={A}")

dfs(0)
print(ans)