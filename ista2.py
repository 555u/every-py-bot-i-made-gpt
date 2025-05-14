import requests
import time
import os

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            return True  # Username is available
        else:
            return False  # Username is taken
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to check {username}: {e}")
        return False

def main():
    input_file = "number_letter_combinations.txt"
    output_file = "available_usernames.txt"
    
    if not os.path.exists(input_file):
        print(f"[ERROR] File '{input_file}' not found. Make sure it's in the same directory as this script.")
        return
    
    with open(input_file, "r") as f:
        usernames = [line.strip() for line in f]
    
    available_usernames = []
    
    for username in usernames:
        if check_username(username):
            print(f"[AVAILABLE] {username}")
            available_usernames.append(username)
        else:
            print(f"[TAKEN] {username}")
        
        time.sleep(1)  # Delay to avoid rate limiting
    
    with open(output_file, "w") as f:
        f.write("\n".join(available_usernames))
    
    print(f"Done! Check '{output_file}' for results.")

if __name__ == "__main__":
    main()