import sys

input = sys.stdin.readline

def is_vowel(c):
    vowel = "aeiou"
    return c in vowel

while True:
    s = input().strip()
    if s == "end":
        break
    
    is_acceptable = True
    if not any(is_vowel(c) for c in s):
        is_acceptable = False
    
    cnt, vowel_flag = 0, False
    for i, c in enumerate(s):
        if i == 0:
            cnt = 1
            vowel_flag = is_vowel(c)
            continue
        
        if vowel_flag == is_vowel(c):
            cnt += 1
        else:
            cnt = 1
            vowel_flag = is_vowel(c)
        
        if cnt >= 3:
            is_acceptable = False
            break
    
    last_char = ''
    for c in s:
        if last_char == c:
            if c not in 'eo':
                is_acceptable = False
                break
        
        last_char = c
    
    if is_acceptable:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
