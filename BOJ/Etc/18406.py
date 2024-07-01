s = input()
def func(s):
    return sum(map(int, s))
print("LUCKY" if func(s[:len(s)//2]) == func(s[len(s)//2:]) else "READY")
