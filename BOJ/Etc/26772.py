heart = [
    ' @@@   @@@ ',
    '@   @ @   @',
    '@    @    @',
    '@         @',
    ' @       @ ',
    '  @     @  ',
    '   @   @   ',
    '    @ @    ',
    '     @     '
]

n = int(input().strip())
for line in heart:
    print((line + ' ') * n)
