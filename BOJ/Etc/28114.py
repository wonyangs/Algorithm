d=[input().split()for _ in range(3)]
print(*sorted(int(y)%100 for _,y,_ in d),sep='')
print(''.join(s[0]for _,_,s in sorted(d,key=lambda x:-int(x[0]))))
