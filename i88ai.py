import aiohttp
import asyncio
import string
import time
import random

# Function to generate usernames in the format mr0x
def generate_usernames():
    letters = string.ascii_lowercase + string.ascii_uppercase  # All letters
    digits = string.digits  # Digits from 0 to 9
    for digit in digits:
        for letter in letters:
            yield f"mr{digit}{letter}"

# Function to check if a username exists on Instagram asynchronously
async def check_username_availability(session, username):
    url = f"https://www.instagram.com/{username}/"
    try:
        async with session.get(url) as response:
            return username, response.status == 404  # If status is 404, username is available
    except Exception as e:
        print(f"Error checking {username}: {e}")
        return username, False

# Function to check and save available usernames asynchronously
async def check_and_save_usernames():
    available_usernames = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        
        # Generate the usernames and check availability concurrently
        for username in generate_usernames():
            tasks.append(asyncio.ensure_future(check_username_availability(session, username)))
        
        # Await all tasks
        results = await asyncio.gather(*tasks)

        # Filter out available usernames and save them to a file
        for username, is_available in results:
            if is_available:
                print(f"Available: {username}")
                available_usernames.append(username)
        
        with open("available_usernames.txt", "w") as file:
            for username in available_usernames:
                file.write(username + "\n")
    
    print(f"Available usernames saved to available_usernames.txt")

# Run the function
start_time = time.time()
asyncio.run(check_and_save_usernames())
print(f"Process completed in {time.time() - start_time} seconds")
