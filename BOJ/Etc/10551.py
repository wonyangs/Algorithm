keys = [
    "1QAZ",
    "2WSX",
    "3EDC",
    "45RTFGVB",
    "67YUHJNM",
    "8IK,",
    "9OL.",
    "0P[]-=\;'/"
]

cnt = [0] * 8
s = input()

for c in s:
    for i in range(len(keys)):
        if c in keys[i]:
            cnt[i] += 1
            break

for n in cnt:
    print(n)
