def calculate_working_time(time_data):
    start_h, start_m, start_s, end_h, end_m, end_s = time_data
    s = end_s - start_s
    if s < 0:
        s += 60
        end_m -= 1

    m = end_m - start_m
    if m < 0:
        m += 60
        end_h -= 1

    h = end_h - start_h
    return h, m, s


input_data = [list(map(int, input().split())) for _ in range(3)]

for data in input_data:
    h, m, s = calculate_working_time(data)
    print(h, m, s)
