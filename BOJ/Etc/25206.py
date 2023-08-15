total_time = 0
hap = 0
grade_table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 
              'C+':2.5, 'C0':2.0, 
              'D+':1.5, 'D0':1.0, 'F':0 }
for _ in range(20):
    A, time, grade = input().split()
    if grade == 'P':
        continue
    time = float(time)
    grade = grade_table[grade]
    total_time += time
    hap += time * grade
print(hap / total_time)
