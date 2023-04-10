S = input()
i = 0
while i < len(S):
    print(S[i], end='')
    i += ord(S[i]) - ord('A') + 1
