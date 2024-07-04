import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == "EOI":
        break
    s = s.lower()
    print("Found" if s.find("nemo") != -1 else "Missing")
