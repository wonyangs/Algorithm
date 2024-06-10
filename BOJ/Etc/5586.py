S = input()

def c(s):
    cnt = 0
    for i in range(len(S) - 2):
        if s == S[i:i+3]:
            cnt += 1
    return cnt

print(c("JOI"))
print(c("IOI"))
