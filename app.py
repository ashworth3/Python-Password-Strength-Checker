import string

def check_password(password):
    messages = []
    score = 0

    # At least 8 characters long
    if len(password) >= 8:
        score += 2
    else:
        messages.append("Password must be at least 8 characters long.")

    # At least one uppercase letter
    if any(char.isupper() for char in password):
        score += 2
    else:
        messages.append("Password must contain at least one uppercase letter.")

    # At least one lowercase letter
    if any(char.islower() for char in password):
        score += 2
    else:
        messages.append("Password must contain at least one lowercase letter.")

    # At least one digit
    if any(char.isdigit() for char in password):
        score += 2
    else:
        messages.append("Password must contain at least one digit.")

    # At least one special character
    special_characters = string.punctuation
    if any(char in special_characters for char in password):
        score += 2
    else:
        messages.append("Password must contain at least one special character.")

    #Results
    print("\nPassword Strength Check Results:")
    if(score == 10):
        print("Your password is strong! ✅")
    else:
        for message in messages:
            print(message)

    print(f"Password Score: {score}/10")

# Collect user input
print("Welcome to the Password Strength Checker!")
inputPassword = input("Enter password to test: ")
check_password(inputPassword)