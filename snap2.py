import time
import random
import string

def generate_username():
    # Generate a random 4-letter username
    return ''.join(random.choices(string.ascii_lowercase, k=4))

def check_snap_username(username):
    # Simulated API request (replace with actual API logic if available)
    return random.choice([True, False])  # Simulate available/unavailable

def find_available_usernames(tries=50):
    for i in range(tries):
        username = generate_username()
        available = check_snap_username(username)
        status = "AVAILABLE" if available else "Taken"
        print(f"Try {i+1}: Username '{username}' is {status}")
        time.sleep(2)  # Avoid spamming requests

# Example usage
find_available_usernames()
