import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 移動した鳩の情報の保持方法
# 鳩/巣が1/1の場合、変数保持しない
# Q回のループでクエリを処理する

N, Q = list(input().split())
Nest_index = {i: [i] for i in range(1, int(N)+1)}

for _ in range(int(Q)):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 鳩に対応する巣の値を書き換える
        Nest_index[query[2]] = query[1]
        print(Nest_index)
    else:
        count = sum(1 for value in Nest_index.values() if len(value) >= 2)
        print(count)