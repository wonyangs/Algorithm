print(*["Yes" if (s:=input().lower())==s[::-1] else "No" for _ in range(int(input()))], sep="\n")
