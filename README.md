# 🇳🇮 NICWA: Nicaraguan Financial Assistant (Telegram Bot)

**NICWA** is a lightweight, interactive Telegram bot built to streamline currency exchange tracking and conversions (USD/NIO) in Nicaragua. It provides users with up-to-date rates from major local banks and executes precise conversions using real-world buying/selling financial logic.

---

## ✨ Key Features

*   **Multi-Bank Support:** Designed to process and display exchange rates from Nicaragua's top financial institutions (BAC, Banpro, Lafise, Ficohsa, BDF) alongside the official rate from the Central Bank of Nicaragua (BCN).
*   **Smart Financial Logic:** The conversion engine automatically applies the appropriate rate based on user intent—applying the **Buy rate** when converting USD to NIO, and the **Sell rate** when converting NIO to USD.
*   **Stateful User Flow:** Implements robust user session management, allowing seamless, consecutive calculations without requiring bot restarts.
*   **Modern UI/UX:** Built entirely around dynamic `InlineKeyboardMarkup` buttons, offering a clean, menu-driven interface that eliminates the need for users to memorize slash commands.

---

## 🛠️ Tech Stack & Libraries

*   **Language:** Python 3.x
*   **Telegram Framework:** `pyTelegramBotAPI` (Telebot)
*   **Environment Management:** `python-dotenv` (for secure configuration)

---

## ⚙️ Quick Start & Installation

To run a copy of this bot locally for development and testing, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/nicwa-bot.git](https://github.com/YOUR_USERNAME/nicwa-bot.git)
cd nicwa-bot
