w = input()
n = sum(ord(c) - (96 if c.islower() else 38) for c in w)
print("It is a prime word." if n == 1 or all(n % i for i in range(2, int(n**0.5) + 1)) else "It is not a prime word.")
