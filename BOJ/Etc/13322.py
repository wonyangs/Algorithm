import sys

s = sys.stdin.readline().strip()
sys.stdout.write('\n'.join(map(str, range(len(s)))) + '\n')
