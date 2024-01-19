N, cmd = input().split()

N = int(N)
if cmd == "miss":
    print(0)
elif cmd == "bad":
    print(N * 200)
elif cmd == "cool":
    print(N * 400)
elif cmd == "great":
    print(N * 600)
else:
    print(N * 1000)
