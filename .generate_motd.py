from random import randint as ri

choice = ri(0, 12)

if choice <= 5:
    motd = 'Hello'
elif choice <= 7:
    motd = 'Hello'
elif choice == 8:
    motd = 'Hello'
elif choice <= 10:
    motd = 'Hello'
elif choice == 11:
    motd = 'Connection Failed.'
elif choice == 12:
    motd = "Hello"

print(motd)
