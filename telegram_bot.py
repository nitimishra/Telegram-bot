import telebot
import random
import string

# Your bot's token
Token = "<ENTER_YOUR_TOKEN>"
bot = telebot.TeleBot(Token)

# Function to generate a random password
def generate(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    pun = string.punctuation
    all_characters = lower + upper + num + pun
    password = ''.join(random.sample(all_characters, length))
    return password


# Handler for /start and /hello commands
@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.reply_to(message, "Welcome to the bot! Use /password <length> to generate a password.")

# Dictionary to store passwords temporarily
user_passwords = {}

# Handler for /password command
@bot.message_handler(commands=['password'])
def password(message): 
    try:
        # Extract length from the message
        length = int(message.text.split()[1])
        if length < 1:
            raise ValueError("Length must be at least 1.")
        
        # Generate 5 passwords
        passwords = [generate(length) for i in range(5)]
        
        # Save passwords for the user
        user_passwords[message.chat.id] = passwords

        # Format the passwords list with options
        password_options = [f"{i+1}. {pw}" for i, pw in enumerate(passwords)]
        password_options.append("Please reply with the number of the password you want to choose.")

        # Send the passwords as a single message
        bot.reply_to(message, "\n".join(password_options))
    except (IndexError, ValueError):
        bot.reply_to(message, "Please provide a valid length. Example: /password 12")

# Handler for user responses to select a password
@bot.message_handler(func=lambda message: message.chat.id in user_passwords and message.text.isdigit())
def select_password(message):
    try:
        choice = int(message.text) - 1  # Convert choice to zero-based index
        if 0 <= choice < len(user_passwords[message.chat.id]):
            selected_password = user_passwords[message.chat.id][choice]
            bot.reply_to(message, f"You selected: {selected_password}")
            del user_passwords[message.chat.id]  # Clear user's passwords after selection
        else:
            bot.reply_to(message, "Invalid selection. Please enter a valid number.")
    except ValueError:
        bot.reply_to(message, "Please enter a valid number.")

# Start polling for messages
bot.polling()

