p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
agg_p = p1 + p2
agg_s = s1 + s2

if agg_p > agg_s or (agg_p == agg_s and p2 > s1):
    print("Persepolis")
elif agg_s > agg_p or (agg_p == agg_s and s1 > p2):
    print("Esteghlal")
else:
    print("Penalty")
