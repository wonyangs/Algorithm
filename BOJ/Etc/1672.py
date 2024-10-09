t = {('A','A'):'A',('A','G'):'C',('A','C'):'A',('A','T'):'G',('G','A'):'C',('G','G'):'G',('G','C'):'T',('G','T'):'A',('C','A'):'A',('C','G'):'T',('C','C'):'C',('C','T'):'G',('T','A'):'G',('T','G'):'A',('T','C'):'G',('T','T'):'T'}
n, s = int(input()),input().strip(); r=s[-1]
for i in range(n-2,-1,-1):
    r=t[(s[i], r)]
print(r)
