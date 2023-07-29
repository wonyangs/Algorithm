HH, MM = map(int, input().split())
start_H = 9
start_M = 0
diff_H = HH - start_H
diff_M = MM - start_M
print(diff_H * 60 + diff_M)
