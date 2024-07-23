scores = [int(input()) for _ in range(10)]
total = 0

for score in scores:
    total += score
    if total >= 100:
        if total - 100 <= 100 - (total - score):
            print(total)
        else:
            print(total - score)
        break
else:
    print(total)
