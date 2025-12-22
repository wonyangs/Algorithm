t = int(input())
v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for i in range(1, t + 1):
    c = input()
    l = c[-1]
    
    if l.lower() == 'y':
        r = "nobody"
    elif l in v:
        r = "a queen"
    else:
        r = "a king"
        
    print(f"Case #{i}: {c} is ruled by {r}.")
