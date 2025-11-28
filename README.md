🤖 Telegram AI Chatbot Template (Local LLM via Ollama)

A robust, privacy-focused starter template for developers looking to build a Telegram chatbot powered by locally hosted Large Language Models (LLMs).

This project bridges Telegram's Bot API with Ollama's local API, allowing you to run powerful AI models (like Llama 3 or DeepSeek) on your own hardware with zero API costs and 100% data privacy.

🚀 Key Features

🔒 Privacy First: No data is sent to third-party AI clouds (OpenAI/Anthropic). Everything runs on your machine.

🧠 Multi-Model Support: Logic included to switch between models on the fly (e.g., General chat vs. Coding assistant).

💾 Persistent Context: Uses MySQL to store chat history, allowing the bot to remember previous interactions.

Queue Management: Built-in basic limitation system to prevent server overload from multiple users.

Ollama API Example: A clear implementation of how to send JSON requests to the Ollama endpoint using Python requests.

🛠️ Tech Stack

Language: Python

AI Backend: Ollama (running locally)

Database: MySQL (for user history storage)

Interface: pyTelegramBotAPI

📋 Prerequisites

Before running the bot, ensure you have the following installed:

Python 3.8+

MySQL Server (XAMPP, WAMP, or native installation)

Ollama

Telegram Bot Token: Get one from @BotFather on Telegram.

⚙️ Installation & Setup

1. Clone the Repository

git clone [https://github.com/Ashmil-Kurikkal/Telegram-AI-Chat-Bot.git](https://github.com/Ashmil-Kurikkal/Telegram-AI-Chat-Bot.git)
cd Telegram-AI-Chat-Bot


2. Install Dependencies

pip install pyTelegramBotAPI requests mysql-connector-python pyfiglet


3. Database Configuration

You must create the database and table before running the script. Open your MySQL client and run the following SQL commands:

CREATE DATABASE telegram_bot_db;

USE telegram_bot_db;

CREATE TABLE users (
    username VARCHAR(255),
    user_id VARCHAR(255) PRIMARY KEY,
    history JSON
);


4. Pull the AI Models

This bot is configured to use specific models. Open your terminal and pull them via Ollama:

ollama pull llama3
ollama pull deepseek-coder

# Optional: Pull 'llama2-uncensored' if you wish to use option 1 in the menu
ollama pull llama2-uncensored


5. Add Assets

Place an image named logo1.jpg in the root directory of the project. This image is sent to users when they type /start.

🚀 Usage

1. Start Ollama

Ensure the Ollama server is running.

ollama serve


2. Run the Bot

python main.py


3. Configure on Launch

The script uses an interactive setup. When you run it, you will be prompted to enter:

MySQL Username & Password

Database Name (e.g., telegram_bot_db)

Ollama API Port (Default is usually http://127.0.0.1:11434/api/chat)

Telegram Bot Token

Owner Name & Description (Used for the bot's system prompt)

4. Chat

Open Telegram, find your bot, click Start, and use the /ailice command to begin the session.

🧩 Understanding the Code (Ollama Integration)

Many developers struggle with the Ollama API structure. This template demonstrates the correct way to structure the request in Python:

# Snippet from main.py
response = requests.post(
    "[http://127.0.0.1:11434/api/chat](http://127.0.0.1:11434/api/chat)", 
    json={
        "model": "llama3", 
        "messages": [{"role": "user", "content": "Hello!"}], 
        "stream": True 
    }, 
    stream=True
)


endpoint: /api/chat is used for conversational history (as opposed to /api/generate).

stream=True: Essential for handling long responses without timeouts, though this bot currently accumulates the stream before sending the final message to Telegram.

🤝 Contributing

Contributions are welcome! If you want to add .env file support, improve the queuing system, or add Docker support, feel free to fork the repo and submit a pull request.

📜 License

Distributed under the MIT License. See LICENSE for more information.

Created by Ashmil-Kurikkal
