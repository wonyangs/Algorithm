P = int(input())
patterns = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]
for result in [input().strip() for _ in range(P)]:
    print(" ".join(str(sum(result[i:i+3] == p for i in range(38))) for p in patterns))
