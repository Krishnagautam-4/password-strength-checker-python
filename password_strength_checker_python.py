password = input("Enter your password: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score <= 2:
    print("Password Strength: Weak")
elif score == 3 or score == 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
