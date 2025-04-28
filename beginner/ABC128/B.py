import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# strとintのデータを①アルファベット順②点数順に並べ替える
# データの保持方法を考える必要あり
N = int(input())
guide_book = [list(input().split()) for _ in range(N)]
sort_list = sorted(guide_book, key=lambda x: (x[0], -int(x[1])))

[print(guide_book.index(sort_list[i]))+1 for i in sort_list]

# AIによる解説
N = int(input())
restaurants = []
# 入力データを[市名, 点数, 元の順番]の形式で保存
for i in range(N):
    city, score = input().split()
    restaurants.append([city, int(score), i+1])

# 市名でソート（昇順）、点数でソート（降順）
restaurants.sort(key=lambda x: (x[0], -x[1]))

# 元の順番（インデックス）を出力
for restaurant in restaurants:
    print(restaurant[2])
