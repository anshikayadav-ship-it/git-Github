import re

password = input("Enter your password: ")
score = 0
suggestions = []
special_characters = set("@#$%&*!")

# 1. Imp Case Checks
if password == "":
    print("Password cannot be empty.")
    exit()

if " " in password:
    print("Password must not contain spaces.")
    exit()

# 2. Rule Checks & Suggestion Collection
if len(password) >= 8:
    score += 1
else:
    suggestions.append("use at least 8 characters")

if re.search(r'[A-Z]', password):
    score += 1
else:
    suggestions.append("add an uppercase letter")

if re.search(r'[a-z]', password):
    score += 1
else:
    suggestions.append("add a lowercase letter")

if re.search(r'\d', password):
    score += 1
else:
    suggestions.append("add a digit")

if set(password) & special_characters:
        score += 1
else:
        suggestions.append("add a special character")

# 3. Strength Classification
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

# 4. Final Output Display
print(f"Strength: {strength} ({score}/5)")

if suggestions:
    print("Suggestions: " + ", ".join(suggestions))
else:
    print("No suggestions. Your password is secure.")
