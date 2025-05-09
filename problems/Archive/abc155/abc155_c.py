n = int(input())
counts = {}

for i in range(n):
    v = input()
    if v not in counts:
        counts[v] = 1
    else:
        counts[v] += 1

max_val = max(counts.values())
[print(v) for v in sorted([kv[0] for kv in counts.items() if kv[1] == max_val])]