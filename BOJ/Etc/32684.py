scores = [13, 7, 5, 3, 3, 2]
cho, han = [sum(x * y for x, y in zip(map(int, input().split()), scores)) for _ in range(2)]
print("cocjr0208" if cho > han + 1.5 else "ekwoo")
