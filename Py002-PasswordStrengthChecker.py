# Python Password Strength Checker

print("Welcome to the password strength checker")

password = input("Enter your password:\n")
strength = 0

# Check length
if len(password) >= 8:
    print("Password has at least 8 characters ✔️\n")
    strength += 1
else:
    print("Password has at least 8 characters ❌\n")

# Check uppercase letters
if any(char.isupper() for char in password):
    print("Password has at least one uppercase letter ✔️\n")
    strength += 1
else:
    print("Password has at least one uppercase letter ❌\n")

# Check lowercase letters
if any(char.islower() for char in password):
    print("Password has at least one lowercase letter ✔️\n")
    strength += 1
else:
    print("Password has at least one lowercase letter ❌\n")

# Check digits
if any(char.isdigit() for char in password):
    print("Password has at least one number ✔️\n")
    strength += 1
else:
    print("Password has at least one number ❌\n")

# Check special characters
special_chars = "!@#$%^&*()_+-=/*`~"
if any(char in special_chars for char in password):
    print("Password has at least one symbol ✔️\n")
    strength += 1
else:
    print("Password has at least one symbol ❌\n")

# Display strength result
print(f"Strength of your password is {strength}/5\n")

if strength < 3:
    print("Your password is weak!\n")
elif strength == 3:
    print("Your password is average!\n")
else:
    print("Your password is strong!\n")