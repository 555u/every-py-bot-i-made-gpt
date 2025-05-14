import requests
    from bs4 import BeautifulSoup

def check_youtube_username(username):
    url = f"https://www.youtube.com/@{username}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code == 404:  
        return f"✅ Username '{username}' is **available**!"
    elif response.status_code == 200:
        return f"❌ Username '{username}' is **taken**."
    else:
        return f"⚠️ Could not check '{username}', status code: {response.status_code}"

# Load usernames from file
with open("usernames.txt", "r") as file:
    usernames = [line.strip() for line in file]

# Check each username
for username in usernames:
    print(check_youtube_username(username))
