while (s := input().strip()) != "*":
    print("Y" if set("abcdefghijklmnopqrstuvwxyz") <= set(s) else "N")
