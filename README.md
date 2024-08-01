# README.md

## Project: Telegram Group Management Bot

### Overview

This project involves creating a Telegram bot that manages user membership in a Telegram group. The bot is designed to automatically save new members to a SQLite database and remove members from the database when they leave the group. This functionality is useful for keeping track of group membership and ensuring that the database is always up-to-date with the current group members.

### Features

1. **Automatic User Management:**
   - When a new user joins the Telegram group, the bot adds their information (user ID and username) to the SQLite database.
   - When a user leaves the group, the bot removes their information from the database.

2. **Admin-Only Commands:**
   - Only users with admin rights in the group can trigger the bot's functionality. This ensures that unauthorized users cannot modify the database.

3. **SQLite Database Integration:**
   - The bot uses SQLite to store user data, ensuring that the user information is kept in a persistent and easily manageable format.

### Files

1. **`bot.py`:** Contains the main logic for interacting with the Telegram API and handling user events (joining and leaving the group). This file also includes database operations to add and remove users.

2. **`database.py`:** Provides functions to manage the SQLite database, including creating connections, adding users, removing users, and retrieving user information.

3. **`config.py`:** Holds configuration details such as the Telegram bot token and admin user IDs. This file should be updated with your actual bot token and the IDs of the group admins.

### Setup

1. **Install Dependencies:**
   - Make sure you have Python 3.x installed.
   - Install the required libraries using pip:
     ```bash
     pip install pyTelegramBotAPI
     ```

2. **Configuration:**
   - Open `config.py` and replace `'YOUR_TELEGRAM_BOT_TOKEN_HERE'` with your actual Telegram bot token obtained from BotFather.
   - Update the `ADMIN_IDS` list with the user IDs of the admins who will have control over the bot.

3. **Run the Bot:**
   - Ensure that the `database.py` file is executed first to set up the database.
   - Run `bot.py` to start the bot:
     ```bash
     python bot.py
     ```

### Usage

- The bot will automatically start monitoring the group for new members and members who leave.
- When a new user joins, their ID and username are saved in the database.
- When a user leaves, their information is removed from the database.
- The bot operates based on events from the Telegram group and does not require manual input beyond configuration.

### License

This project is provided as-is. Use it according to your own needs and modify it as necessary. No warranties or guarantees are provided.
