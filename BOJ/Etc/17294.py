k = input().strip()
if len(k) <= 2: print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    d = int(k[1]) - int(k[0])
    for i in range(1, len(k) - 1):
        if int(k[i + 1]) - int(k[i]) != d:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
