# Solved on 2020.12.17
# 1620 나는야 포켓몬 마스터 이다솜


import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    p_list = []
    p_dict = {}
    append = p_list.append
    for i in range(n):
        name = input().strip()
        append(name)
        p_dict[name] = i+1

    for i in range(m):
        q = input().strip()
        if q.isalpha():
            sys.stdout.write(str(p_dict[q])+'\n')
        else:
            sys.stdout.write(p_list[int(q)-1]+'\n')


main()
