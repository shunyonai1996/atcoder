import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# スイッチN 電球M
# 2行目から(最終行-1)行目 i番目の電球と繋がってるスイッチのdata
# i番目の電球に繋がってるスイッチ群がdata(1:)
# data(1:)のONのスイッチ数%2==Pなら点灯

# スイッチと電球の接続関係
# S[i] => [電球[sia],電球[sib]...]で表せる？表せるとして、ON/OFFの状態をどうやって解釈する？

# 電球に対応するスイッチをマッピングするデータ
# 全てのスイッチのON/OFFの組み合わせデータ

# スイッチのON/OFFの組み合わせ分ループ(bit全探索)
# Pが全て点灯している数をカウントアップする



N, M = list(map(int, input().split()))
print(f"[DEBUG] スイッチ数 N={N}, 電球数 M={M}")

# スイッチごとに繋がっている電球情報を受け取る
S = []
for i in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    connected = [i-1 for i in data[1:]]
    S.append(connected)
    print(f'スイッチ{i}は{connected}の電球に対応')


# bit全探索



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
