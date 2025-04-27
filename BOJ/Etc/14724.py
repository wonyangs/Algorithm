n = int(input())
c = max((max(map(int, input().split())), i) for i in range(9))
print(["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT",
       "MOTION", "SPG", "COMON", "ALMIGHTY"][c[1]])
