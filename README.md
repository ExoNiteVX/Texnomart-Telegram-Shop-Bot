# 🛒 Texnomart Scraper Bot

---

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram%203.x-26A5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Web Scraping](https://img.shields.io/badge/Scraper-BeautifulSoup4-004d40?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAMUlEQVQ4T2NkYGA4wwAFDAwM/0E0shigAGYIsisYmRiI0YQuQCwYhM0hFAyC5BAKBvEAsX8QCwwS6F0AAAAASUVORK5CYII=)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

---
An automated Telegram bot designed to fetch real-time product data from the Texnomart electronics store. It allows users to browse categories, see current prices, and view installment plans directly within Telegram.

📖 Table of Contents
How It Works

Key Features

Project Structure

Prerequisites

Installation & Setup

Technical Explanation

🤖 How It Works
The bot operates in three main stages:

User Interaction: The user selects a category (e.g., "IPHONE") via a ReplyKeyboardMarkup.

Web Scraping: The bot uses BeautifulSoup4 to request the specific catalog page from Texnomart.

Delivery: The bot parses the HTML, extracts images and prices, and sends them as a series of photo messages.

✨ Key Features
⚡ Asynchronous Handling: Built with aiogram 3.x for non-blocking message processing.

📦 Automated Parsing: No manual database updates needed; it fetches live site data.

💳 Price Breakdown: Displays both the full price and the monthly installment (credit) price.

🎨 HTML Formatting: Clean, bold text layouts for better readability.

📂 Project Structure
main.py: The heart of the bot. Contains message handlers and the main polling loop.

parser.py: The logic responsible for connecting to the website and extracting data.

configs.py: Stores category mappings and keyboard configurations.

.env: (User-created) Stores sensitive tokens and host URLs.

⚙️ Prerequisites
Before running, ensure you have:

Python 3.10 or higher.

A Telegram Bot Token (from @BotFather).

🚀 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/texnomart-bot.git
cd texnomart-bot
Install requirements:

Bash
pip install aiogram requests beautifulsoup4 python-dotenv
Configure the Environment: Create a .env file and add your credentials:

Фрагмент кода
TOKEN=123456789:ABCDEF...
URL=https://texnomart.uz/
HOST=https://texnomart.uz
Start the Bot:

Bash
python main.py
🛠 Technical Explanation
🧠 The Scraper (tilvizr function)
The scraper uses the requests library with a user-agent header to mimic a real browser. It targets specific CSS classes on the Texnomart website:

.product-link: To find the product image source.

.installment-price: To extract the monthly payment plan.

.product-price__current: To get the final cash price.

⌨️ Dynamic Keyboards
The buttons_category function generates buttons dynamically based on the CATEGORIES dictionary. This means you can add a new category to your config file, and it will automatically appear in the bot without changing the UI code.

⏳ Anti-Flood Measures
The code includes a small time.sleep(0.5) (Note: In production, asyncio.sleep is preferred) between sending photos to prevent the Telegram API from rate-limiting the bot when sending many products at once.
