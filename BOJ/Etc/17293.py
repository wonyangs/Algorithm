n = int(input())
def b(x):
    return 'no more bottles' if x == 0 else ('1 bottle' if x == 1 else f'{x} bottles')
for k in range(n, 0, -1):
    print(f"{b(k).capitalize()} of beer on the wall, {b(k)} of beer.")
    print(f"Take one down and pass it around, {b(k-1)} of beer on the wall.")
    print()
print("No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {b(n)} of beer on the wall.")
