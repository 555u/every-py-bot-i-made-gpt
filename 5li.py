import random
import string

def generate_usernames(count=500):
    usernames = set()

    while len(usernames) < count:
        if random.random() < 0.5:
            username = f"{random.randint(1000, 9999)}{random.choice(string.ascii_lowercase)}"
        else:
            username = f"{random.randint(10000, 99999)}{random.choice(string.ascii_lowercase)}"
        
        usernames.add(username)

    with open("usernames.txt", "w") as file:
        file.write("\n".join(usernames))

    print(f"✅ Generated {len(usernames)} usernames and saved to 'usernames.txt'.")

generate_usernames()
