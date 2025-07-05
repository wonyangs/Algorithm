n=int(input())
s=input()
low=set('roygbiv')
up=set('ROYGBIV')
sl=set(s)
a=low<=sl
b=up<=sl
print('YeS' if a and b else 'yes' if a else 'YES' if b else 'NO!')
