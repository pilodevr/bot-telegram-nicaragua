# 🇳🇮 NICWA: Nicaraguan Financial Assistant (Telegram Bot)

NICWA is an interactive Telegram bot designed to facilitate access to currency exchange rates (USD/NIO) in Nicaragua. It allows users to check up-to-date rates from the country's main banks and calculate exact conversions applying real buying and selling logic.

---

## ✨ Key Features

* **🏦 Local Banks:** Support for exchange rates from BAC, Banpro, Lafise, Ficohsa, BDF, and the official rate of the Central Bank of Nicaragua (BCN).
* **🔄 Bidirectional Conversion:** Calculates conversions from Dollars to Córdobas (USD to NIO) and from Córdobas to Dollars (NIO to USD).
* **🧮 Real Financial Logic:** The algorithm automatically applies the Buy rate when the user hands over dollars, and the Sell rate when they need to buy dollars.
* **📱 Advanced UX Interface:** Fully guided navigation using `InlineKeyboardMarkup` (buttons integrated directly into the messages), eliminating the need to memorize commands.
* **🔁 Continuous Flow:** User state management allows for multiple consecutive queries without having to restart the bot.

---

## 🚀 Live Demo

*(Here you can add a link to your bot if it is hosted on a server, for example: Try it here on Telegram)*

---

## 🛠️ Technologies Used

* **Language:** Python 3
* **Main Library:** `pyTelegramBotAPI` (Telebot)

---

## ⚙️ Local Installation & Setup

If you want to run this project on your local machine, follow these steps:

### 1. Clone the repository
bash
git clone [https://github.com/your-username/nicwa-bot.git](https://github.com/your-username/nicwa-bot.git)
cd nicwa-bot
### 2. Install the required dependencies
Bash
pip install pyTelegramBotAPI
### 3. Configure your Telegram Token
Open Telegram and search for @BotFather.

Create a new bot using /newbot and copy the provided Token.

Open the bot_financiero.py file (or whatever you named your script) and replace the TOKEN variable:

Python
TOKEN = 'YOUR_TOKEN_GENERATED_BY_BOTFATHER'
### 4. Run the bot
Bash
python bot_financiero.py
📝 Note on Data (API)
Currently, the exchange rates in the source code use a simulation system (mock data) in the obtener_tasas_bancos() function for demonstration purposes. For a production environment, this function can be connected to a Web Scraping script (e.g., BeautifulSoup) or a private API to extract real-time data from Nicaraguan banks.

🔒 Security
Never upload your real Telegram Token to public repositories. Make sure to use environment variables (.env) or hide your Token before committing and pushing your code.

Developed with ☕ by ##pilodevr
