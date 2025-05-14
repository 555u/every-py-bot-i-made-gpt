# 🤖 RH-MultiUserBots Suite

Welcome to **RH-MultiUserBots**, a powerful suite of automated Python bots crafted by **Rashed Humaid Albalushi** to simulate routine brute-force testing and user-list interactions across various platforms — including **YouTube, Snapchat, Discord, Instagram, Gmail**, and **Outlook**.

This project showcases a structured, repeatable methodology for understanding how systems handle login attempts and API-level user data fetching.

---

## 🔁 Routine Workflow

Every bot in this suite follows the same 3-step routine:

### 1. 🧪 Get API Access  
Each bot connects to a platform’s API (either official or simulated/mock for ethical testing). This step handles headers, tokens, and endpoints required for interaction.

### 2. 📜 Fetch/Load User List  
Each bot reads a preloaded user list (could be `.txt`, `.csv`, or in-code list). These users are either targets for automation or entries for simulation.

### 3. 🔐 Brute Simulation (Up to 9000 Attempts)  
Each bot executes a simulated brute-force loop — attempting up to **9000 password guesses per user** using various logic layers (e.g., number-based, dictionary-based, or hybrid).

> ⚠️ **Disclaimer**: This suite is for educational and ethical cybersecurity testing only. It is strictly prohibited to use it against real platforms or users without explicit permission.

---

## 🧰 Bot Collection

Here’s a breakdown of the available bots:

| Bot        | Description                                                  | Script Name         |
|------------|--------------------------------------------------------------|---------------------|
| 🎥 YouTube | Simulates account access attempts through channel emails     | `yt_bot.py`         |
| 👻 Snapchat | Automates username lookups and login routines                | `snap_bot.py`       |
| 💬 Discord  | Simulates brute force on known Discord user handles         | `discord_bot.py`    |
| 📸 Instagram | Uses Instagram-like logic to test logins via handles/emails | `insta_bot.py`      |
| 📧 Gmail     | Simulates Google login attempts with API token setups       | `gmail_bot.py`      |
| 📬 Outlook   | Tests Microsoft login attempts using mock endpoints         | `outlook_bot.py`    |

---

## 🛠️ Requirements

Install the dependencies before running:

```bash
pip install -r requirements.txt
