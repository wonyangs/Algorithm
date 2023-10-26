T = int(input())
scores = list(map(int, input().split())) + [0] * (5 - T)

result = 0

if scores[0] > scores[2]:
    result += (scores[0]-scores[2])*508
else:
    result += (scores[2]-scores[0])*108

if scores[1] > scores[3]:
    result += (scores[1]-scores[3])*212
else:
    result += (scores[3]-scores[1])*305

if T == 5:
    result += scores[4]*707

result *= 4763

print(result)
