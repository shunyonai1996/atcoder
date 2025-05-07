## 【Python】文字列検索に便利な機能一覧
結論、`chr()`と`ord()`を使ましょう。

以前までは右も左もわからず、`string`というモジュールを使用していました。
https://qiita.com/okkn/items/3aef4458ed2269a59d63

```python
import string
print(string.ascii_letters)
>>> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(string.ascii_lowercase)
>>> 'abcdefghijklmnopqrstuvwxyz'

print(string.ascii_uppercase)
>>> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
標準入力に任意のアルファベットが来た時、次のアルファベットを出力したい時(`a`なら`b`、`z`なら`a`)は以下の実装をしていました。
```python
import string
S = input()
lowers = string.ascii_lowercase
next_index = (lowers.index(S) + 1) % 26
print(lowers[next_index])
```

## Python 3はデフォルトでUnicode対応
これに対応する関数が`ord()`と`chr()`です。
- `ord('A')` → Unicodeコードポイントを返す（結果はASCIIと一致）
- `chr(97)` → Unicodeコードポイントから文字を返す

# a = 97 z = 122 A = 65 Z = 90

🟦 文字コード操作（英小文字 a〜z）
```python
# 次のアルファベット（z→a でループ）
C = input()
print(chr(ord('a') + ((ord(C) - ord('a') + 1) % 26)))

# アルファベットを数値化（'a'→0, ..., 'z'→25）
pos = ord(C) - ord('a')

# 数値をアルファベットに変換（0→'a'）
c = chr(pos + ord('a'))
```

🟩 ビット全探索
```python
N = 3
for bit in range(1 << N):
    pattern = []
    for i in range(N):
        if bit & (1 << i):
            pattern.append(1)  # i番目を採用
        else:
            pattern.append(0)  # i番目を不採用
    print(f"{bit:0{N}b} -> {pattern}")
```

🟨 頻度カウント
```python
from collections import Counter

s = input()
count = Counter(s)
print(count['a'])  # 文字 'a' の出現回数
```

🟧 アルファベットの初期化済みリスト
```python
import string

lower = list(string.ascii_lowercase)   # ['a', 'b', ..., 'z']
upper = list(string.ascii_uppercase)   # ['A', 'B', ..., 'Z']
```

🟥 2次元グリッド探索（上下左右）
```python
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右

for h in range(H):
    for w in range(W):
        for dh, dw in dirs:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W:
                # 移動後の処理
                pass
```

🟪 入力の高速化（TLE対策）
```python
import sys
input = sys.stdin.readline
```

🟫 素数判定（簡易）
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

📘 リスト系ユーティリティ
```python
# 平坦なリストを作成（[0]*N）
a = [0] * 10

# 2次元リストの初期化
grid = [[0]*W for _ in range(H)]

# 和・最大・最小
sum(a), max(a), min(a)

# ソート（降順）
a.sort(reverse=True)
```