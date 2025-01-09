from math import factorial as f
e = 0
print("n e\n- -----------")
for n in range(10):
    e += 1 / f(n)
    print(f"{n} {['1', '2', '2.5'][n] if n < 3 else f'{e:.9f}'}")
