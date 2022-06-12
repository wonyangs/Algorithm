def solution(p):
    length = len(p)
    count = [0] * length

    for i in range(length-1):
        MIN = min(p[i+1:length])
        if p[i] < MIN:
            continue
        for j in range(i, length):
            if p[j] == MIN:
                p[i], p[j] = p[j], p[i]
                count[i] += 1
                count[j] += 1
                break
    return count
