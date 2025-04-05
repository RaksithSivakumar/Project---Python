import re

def check_password_strength(password):
    strength_level = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        strength_level += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_level += 1
    else:
        suggestions.append("Include at least one uppercase letter (A-Z).")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_level += 1
    else:
        suggestions.append("Include at least one lowercase letter (a-z).")
    
    # Check for digits
    if re.search(r'[0-9]', password):
        strength_level += 1
    else:
        suggestions.append("Include at least one digit (0-9).")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_level += 1
    else:
        suggestions.append("Include at least one special character (e.g., !@#$%^&*).")
    
    return strength_level, suggestions

def evaluate_password_strength(password):
    strength_level, suggestions = check_password_strength(password)
    
    if strength_level == 5:
        print("Your password is strong! 🎉")
    elif strength_level >= 3:
        print("Your password is moderate. Consider improving it:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password is weak. Please improve it by following these suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

def password_strength_checker():
    print("Welcome to the Password Strength Checker!")
    
    # Get password from the user
    password = input("Enter your password: ")
    
    # Evaluate the password strength
    evaluate_password_strength(password)

if __name__ == "__main__":
    password_strength_checker()
