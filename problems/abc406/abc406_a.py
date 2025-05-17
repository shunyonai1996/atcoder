A, B, C, D = map(int, input().split())

if A < C:
    print('No')
elif A == C:
    if D <= B:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')