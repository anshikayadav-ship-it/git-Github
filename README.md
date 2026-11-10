# Password Strength Checker 🔒

A Python application designed to evaluate password security against standard cryptographic complexity criteria, calculate a strength score, and provide real-time actionable feedback.

## 📌 Project Overview
The **Password Strength Checker** evaluates user-submitted passwords using rule-based validation. It scores passwords on a scale of **0 to 5** and classifies them into three categories: **Weak**, **Medium**, or **Strong**. If a password fails any security rule, the program generates specific recommendations to help the user harden their password.

## 🎯 Key Features & Objectives
- **Length Verification:** Ensures passwords meet the minimum threshold of 8 characters.
- **Character Diversity Checks:** Scans for uppercase letters, lowercase letters, numeric digits, and special symbols.
- **Input Sanitization:** Rejects empty inputs and passwords containing spaces.
- **Scoring System:** Calculates a cumulative security score out of 5.
- **Feedback Generation:** Provides real-time suggestions based on failed rules.

## 🛠️ Concepts & Technologies Used
* **Language:** Python 3
* **Standard Modules:** `re` (Regular Expressions)
* **Data Structures:** `Strings`, `Lists`, `Sets`
* **Control Flow:** `if / elif / else` conditional blocks
* **Pattern Matching:** Regex character class searching (`[A-Z]`, `[a-z]`, `\d`)
* **Set Operations:** Set intersection (`&`) for special character lookup


## 📏 Security Rules & Scoring Criteria
| Rule # | Requirement | Validation Method | Points |
| :---: | :--- | :--- | :---: |
| **1** | Minimum 8 characters | String length check (`len >= 8`) | +1 |
| **2** | At least 1 Uppercase Letter | Regular Expression (`[A-Z]`) | +1 |
| **3** | At least 1 Lowercase Letter | Regular Expression (`[a-z]`) | +1 |
| **4** | At least 1 Numeric Digit | Regular Expression (`\d`) | +1 |
| **5** | At least 1 Special Character (`@#$%&!`) | Set Intersection (`set & set`) | +1 |

### 📊 Strength Classification

| Score | Rating | Output Message |
| :---: | :---: | :--- |
| **0 – 2** | 🔴 **Weak** | Needs significant improvement |
| **3 – 4** | 🟡 **Medium** | Acceptable, but room for hardening |
| **5** | 🟢 **Strong** | Maximum security achieved |

> **Note:** Passwords that are completely empty or contain spaces are flagged as **Invalid Input** and skipped prior to scoring.

## 🧪 Test Cases & Expected Outputs

| Input | Classification | Score | Output / Suggestions |
| :--- | :---: | :---: | :--- |
| `abc123` | **Weak** | 2/5 | *Suggestions: use at least 8 characters, add an uppercase letter, add a special character* |
| `Hello123` | **Medium** | 4/5 | *Suggestions: add a special character* |
| `""` *(empty)* | **Invalid** | — | *Password cannot be empty.* |
| `Hello 123` | **Invalid** | — | *Password must not contain spaces.* |
| `Hello@123Xy` | **Strong** | 5/5 | *No suggestions. Your password is secure.* |
