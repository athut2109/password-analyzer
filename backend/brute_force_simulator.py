import math
import string

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    entropy = len(password) * math.log2(charset) if charset > 0 else 0
    return entropy

def estimate_crack_time(entropy):
    guesses_per_second = 1e9  # 1 billion guesses per second
    seconds = 2 ** entropy / guesses_per_second

    if seconds < 60:
        return "Less than a minute"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds // 86400)} days"
    else:
        return f"{int(seconds // 31536000)} years"

def get_strength(entropy):
    if entropy < 28:
        return "Weak"
    elif entropy < 50:
        return "Medium"
    else:
        return "Strong"
