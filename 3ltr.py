import random
import string

def generate_usernames(count=5000):
    chars = string.ascii_lowercase + string.digits  # a-z and 0-9
    usernames = set()

    while len(usernames) < count:
        username = "".join(random.choices(chars, k=3))
        usernames.add(username)  

    with open("usernames.txt", "w") as file:
        file.write("\n".join(usernames))

    print(f"✅ Generated {len(usernames)} usernames and saved to 'usernames.txt'.")

generate_usernames()
