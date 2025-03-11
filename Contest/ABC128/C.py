import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


N, M = list(map(int, input().split()))
# ks = [list(map(int, input().split())) for i in range(N)]

ans = 0

S = []
for _ in range(M):
    k, *switches = map(int, input().split())
    S.append([s-1 for s in switches])  # 0-indexedに変換

P = list(map(int, input().split()))
print(f"[DEBUG] 点灯条件 P={P}")

# 2. 全パターン試行
ans = 0
for state in range(1 << N):  # 全スイッチの状態を試す
    # 各電球をチェック
    for bulb in range(M):
        # その電球に接続されているスイッチのONの数を数える
        on_count = sum(1 for s in S[bulb] if state & (1 << s))
        # 条件を満たさない場合は、このパターンを終了
        if on_count % 2 != P[bulb]:
            break
    else:  # 全ての電球が条件を満たした場合
        ans += 1

print(ans)

exit()

# AIによる解説
# 1. 入力を受け取る
N, M = map(int, input().split())
print(f"[DEBUG] スイッチ数 N={N}, 電球数 M={M}")

# 電球ごとに接続スイッチ情報を受け取る
S = []
for i in range(M):
    # 各行は「k s1 s2 ... sk」という形式
    data = list(map(int, input().split()))
    k = data[0]                   # 電球 i に接続されているスイッチ数
    connected = data[1:]          # 実際に接続されているスイッチ番号のリスト
    connected = [s - 1 for s in connected]  # 0-based index に合わせる
    S.append(connected)
    print(f"[DEBUG] 電球{i}に接続 k={k}, スイッチ={connected}")

# 各電球の点灯条件 (cnt % 2 == P[i]) を表す P
P = list(map(int, input().split()))
print(f"[DEBUG] 点灯条件 P={P}")

# 2. 全探索 (ビットマスク)
ans = 0
# 0 ～ (2^N - 1) の全ビットマスクを試す
for mask in range(1 << N):
    # 最初の数パターンだけデバッグ出力してみる
    print(f'mask:{mask} N:{N}')
    print(f"[DEBUG] 現在のmask={mask:0{N}b} (2進表記)")

    ok_count = 0  # 条件を満たした電球の数
    for m in range(M):
        cnt = 0
        # 電球 m に接続されているスイッチを調べる
        for s in S[m]:
            # mask の s ビット目が1なら ON とみなす
            if mask & (1 << s):
                print(1 << s)
                cnt += 1

        # cnt の偶奇が P[m] と一致していれば点灯
        if cnt % 2 == P[m]:
            ok_count += 1

    # M 個すべての電球が点灯条件を満たすか
    if ok_count == M:
        ans += 1

# 3. 結果を出力
print(ans)
