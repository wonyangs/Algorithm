s = input().strip()
schools = {
    "northlondo": "NLCS",
    "branksomeh": "BHA", 
    "koreainter": "KIS",
    "stjohnsbur": "SJA"
}

for n in range(26):
    t = ""
    for c in s:
        t += chr((ord(c) - ord('a') - n) % 26 + ord('a'))
    if t in schools:
        print(schools[t])
        break
