def sleep_duration(go_to_sleep_time, wake_up_time):
    if go_to_sleep_time <= 3:
        return wake_up_time - go_to_sleep_time
    else:
        return (24 - go_to_sleep_time) + wake_up_time

a = int(input())
b = int(input())
res = sleep_duration(a, b)
print(res)
