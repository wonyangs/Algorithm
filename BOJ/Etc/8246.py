a, b, k = map(int, input().split())

def solve(w, h):
    if w < k or h < k:
        return 0
    cnt = w // k
    used = k
    if h >= 2 * k:
        cnt += w // k
        used += k
    rem = h - used
    if rem >= k:
        add = rem // k
        cnt += add
        if w >= 2 * k:
            cnt += add
    return cnt

print(max(solve(a, b), solve(b, a)))
