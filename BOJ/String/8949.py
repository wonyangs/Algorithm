import itertools; print(''.join([str(sum(map(int, tup))) for tup in [tuple(filter(None, y)) for y in itertools.zip_longest(*map(lambda x: list(reversed(x)), input().split()))]][::-1]))
