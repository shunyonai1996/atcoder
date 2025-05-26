N = int(input())
result = [0] * 4

for i in range(N):
    S = input()
    if S == 'AC':
        result[0] += 1
    elif S == 'WA':
        result[1] += 1
    elif S == 'TLE':
        result[2] += 1
    elif S == 'RE':
        result[3] += 1
print(f"AC x {result[0]}")
print(f"WA x {result[1]}")
print(f"TLE x {result[2]}")
print(f"RE x {result[3]}")