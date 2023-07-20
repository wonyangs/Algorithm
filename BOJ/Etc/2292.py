def Floor(RNumber) :
    temp = (RNumber - 1) / 3
    return int(temp ** 0.5 + 0.5) + 1

N = int(input())
print(Floor(N))
