while (s := input()) != '#':
    print(' '.join(w[::-1] for w in s.split(' ')))
