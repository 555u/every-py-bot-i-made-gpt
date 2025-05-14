import random
import string

def generate_email():
    patterns = [
        lambda: f"{random.randint(1000, 9999)}@outlook.com",
        lambda: f"{random.choice(string.ascii_lowercase)}{random.randint(10, 99)}{random.choice(string.ascii_lowercase)}@outlook.com",
        lambda: f"{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_lowercase)}{random.randint(100, 999)}@outlook.com",
        lambda: f"{random.choice('xyz789')}{random.choice('qwe456')}{random.choice('asd123')}{random.choice('zxc098')}@outlook.com",
        lambda: f"{random.choice(string.ascii_letters)}{random.choice(string.digits)}{random.choice(string.ascii_letters)}{random.choice(string.digits)}@outlook.com"
    ]
    return random.choice(patterns)()

emails = [generate_email() for _ in range(500)]

with open("generated_emails.txt", "w") as file:
    file.write("\n".join(emails))

print("500 rare emails generated and saved to generated_emails.txt!")
