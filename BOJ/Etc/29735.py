start, end = input().split()

start_h, start_m = map(int, start.split(':'))
end_h, end_m = map(int, end.split(':'))

left, per_m = map(int, input().split())
left += 1

now_h, now_m = start_h, start_m
day = 0

while left > 0:
    next_m = now_m + per_m
    next_h = now_h
    if next_m >= 60:
        next_m -= 60
        next_h += 1
    
    if next_h > end_h or (next_h == end_h and next_m >= end_m):
        now_h, now_m = start_h, start_m
        day += 1
        continue

    left -= 1
    now_h, now_m = next_h, next_m

print(day)
print("%02d:%02d"%(now_h, now_m))
