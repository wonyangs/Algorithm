words = input()

dic = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}

res = ''
op = []
for word in words:
    if word in dic.keys():
        if not op:
            op.append(word)
        elif word == ')':
            while op:
                tmp = op.pop()
                if tmp == '(':
                    break
                res += tmp
        elif dic[op[-1]] < dic[word] or op[-1] == '(':
            op.append(word)
        else:
            while op:
                if op[-1] == '(' or dic[op[-1]] < dic[word]:
                    break
                tmp = op.pop()
                res += tmp
            op.append(word)
    else:
        res += word

while op:
    tmp = op.pop()
    res += tmp
print(res)
