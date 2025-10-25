# Telegram-bot
# 🔐 Telegram Random Password Generator Bot

A simple **Telegram bot** built using **Python** and the **Telegram Bot API** that generates strong random passwords instantly.  
Just type `/start`, enter the password length you need, and the bot will generate **5 random passwords** — you can choose any one you like!

---

## 🚀 Features

- ✅ Generate **secure random passwords**
- ✅ Choose custom **password length**
- ✅ Get **5 password suggestions** each time
- ✅ Simple and interactive Telegram interface
- ✅ Built with clean and easy-to-read Python code

---

## 🧰 Tech Stack

- **Python 3.x**
- **python-telegram-bot** library
- **random** (Python standard library)
- **string** (Python standard library)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/telegram-password-generator-bot.git
cd telegram-password-generator-bot

### 2️⃣ Install dependencies

```bash
pip install python-telegram-bot

### 3️⃣ Create your Telegram bot

1. Open Telegram and search for **BotFather**  
2. Type `/newbot` and follow the steps to create your bot  
3. Choose a **name** and a **username** for your bot  
4. Once the bot is created, **BotFather** will give you an **API Token**  
5. Copy this token — you’ll need it to connect your bot to your Python script  

> ⚠️ **Important:** Keep your token safe and **do not share it publicly** (it gives full control of your bot).

### 4️⃣ Add your bot token

Create a new file named **`main.py`** in your project directory and add the following code:

```python
Token = "<ENTER_YOUR_TOKEN>"

## ▶️ How to Run

Run the bot using the following command:

```bash
python main.py

📁 Project Structure
telegram-password-generator-bot/
|
├── main.py              # Main bot logic
└── README.md            # Project documentation
