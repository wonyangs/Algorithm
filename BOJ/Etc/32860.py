n, m = map(int, input().split())
if m <= 26:
    print(f"SN {n}{chr(64 + m)}")
else:
    m -= 27
    print(f"SN {n}{chr(97 + m // 26)}{chr(97 + m % 26)}")
