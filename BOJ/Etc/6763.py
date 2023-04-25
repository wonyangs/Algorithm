sl = int(input())
rs = int(input())
ol = rs - sl

if ol <= 0:
    print("Congratulations, you are within the speed limit!")
elif ol <= 20:
    print("You are speeding and your fine is $100.")
elif ol <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
