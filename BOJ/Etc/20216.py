import sys
for l in sys.stdin:
    l = l.strip()
    if l == "I quacked the code!":
        break
    if l.endswith("?"):
        print("Quack!", flush=True)
    elif l.endswith("."):
        print("*Nod*", flush=True)
