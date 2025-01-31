t = {'.':'.','O':'O','-':'|','|':'-','/':'\\','\\':'/','^':'<','<':'v','v':'>','>':'^'}
N, M = map(int,input().split())
p = [input() for _ in range(N)]
for i in range(M):
    print(''.join(t[p[j][M-1-i]] for j in range(N)))
