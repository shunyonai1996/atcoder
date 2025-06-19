H, W = map(int, input().split())

blocks = []
min_block = 100
for i in range(H):
    blocks.append(list(map(int, input().split())))
    min_block = min(min_block, min(blocks[i]))

block_cnt = 0
for i in range(H):
    for j in range(W):
        block_cnt += blocks[i][j] - min_block

print(block_cnt)